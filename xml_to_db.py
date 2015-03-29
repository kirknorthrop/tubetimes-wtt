# -*- coding: utf-8 -*-
#!/usr/bin/python

# London Underground Working Timetable PDF converter
# Created as part of the tubetimes project at http://tubetim.es/
#
# Copyright (c) 2015 Kirk Northrop <kirk@krn.me.uk>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# This software is not endorsed, supported by or linked with London
# Underground or Transport for London in any way.

from bs4 import BeautifulSoup
import re
import sys
from datetime import datetime, timedelta, time
from xlwt import Workbook, easyxf
import linedata
from model import Base, Station, Line, JourneyPatternSection, Route, RouteSection, Service, JourneyPattern, VehicleJourney, ServicePoint, FixedTimeLink, StationCode, NewRoute, NewTimePoint, TrackernetLine, TrackernetStation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Default styles for Tube WTTs
NORMAL_STYLE = easyxf('font: height 140;')
BOLD_STYLE = easyxf('font: height 140, bold true;')
ITALIC_STYLE = easyxf('font: height 140, italic true;')
BOLD_ITALIC_STYLE = easyxf('font: height 140, bold true, italic true;')



### SET LINE HERE
line = linedata.NORTHERN


line_name = line['line_name']
variations = line['variations']
columns = line['columns']
header = line['header']
row_names = line['row_names']
rows = line['rows']


time_regex = re.compile('(\d\d)(\s*[A-Za-z+ ]\s*)(\d\d)(\d\d)?')
strip_tags_regex = re.compile('(.*?)<.+?>(.*?)</.+>(.*?)')


engine = create_engine('postgresql://kirk:@127.0.0.1/tubetimes')# , echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# So we need to create workbooks for all the variations
for variation in variations:
    for day in variations[variation]:
        variations[variation][day]['output'] = Workbook(encoding='utf-8')
        # Then in the state we want to store some things...
        variations[variation][day]['state']['number_of_rows'] = len(rows[variation]['rows'])
        variations[variation][day]['state']['current_column'] = 0

# Get the xml and create the soup
f = open(sys.argv[1], 'r')
print 'Creating soup...'
soup = BeautifulSoup(f)

# Then for each page...
for page in soup.pdf2xml.find_all('page'):

    print 'Processing page ' + page['number']

    page_direction = None
    page_day = None

    # So we want to look in the header and find out which direction/day this is.
    possible_directions = rows.keys()
    for text in page.find_all('text'):
        if int(text['top']) < header:
            for direction in possible_directions:
                if direction in text.renderContents():
                    page_direction = direction
                    break
            for day in linedata.POSSIBLE_DAYS:
                if day in text.renderContents():
                    page_day = day
                    break

    if page_direction and page_day:
        output = [['' for _ in range(len(columns * len(rows[page_direction]['tableoffsets'])))] for _ in range(len(rows[page_direction]['rows']) * len(rows[page_direction]['tableoffsets']))]
        fonts = [[{'bold': False, 'italic': False} for _ in range(len(columns * len(rows[page_direction]['tableoffsets'])))] for _ in range(len(rows[page_direction]['rows']) * len(rows[page_direction]['tableoffsets']))]

        # So for as many tables as we have...
        for offset_index, offset in enumerate(rows[page_direction]['tableoffsets']):
            for text in page.find_all('text'):
                row_no = None
                col_no = None

                for i, col in enumerate(columns):
                    if int(text['left']) < col-1:
                        col_no = i + (len(columns) * offset_index)
                        break

                for i, row in enumerate(rows[page_direction]['rows']):
                    if int(text['top']) < (row + offset) and int(text['top']) < (rows[page_direction]['rows'][len(rows[page_direction]['rows']) - 1] + offset) and int(text['top']) > (rows[page_direction]['rows'][0] + offset):
                        row_no = i
                        break

                if row_no is not None and col_no is not None:
                    cell_value = text.renderContents()

                    if text.find_all(True):
                        if len(text.find_all('b')):
                            fonts[row_no][col_no]['bold'] = True
                        if len(text.find_all('i')):
                            fonts[row_no][col_no]['italic'] = True

                        cell_value = strip_tags_regex.sub('\g<1>\g<2>\g<3>', cell_value)

                    if row_no is not None and col_no is not None and cell_value:
                        output[row_no][col_no] += str(cell_value)

        if variations[page_direction][page_day]['state'].get('column', None) is None or (variations[page_direction][page_day]['state'].get('column') + len(output[0])) > 255:
            ws = variations[page_direction][page_day]['output'].add_sheet('Page ' + page['number'])
            variations[page_direction][page_day]['state']['current_sheet'] = ws
            column_offset = 0
        else:
            ws = variations[page_direction][page_day]['state']['current_sheet']
            column_offset = variations[page_direction][page_day]['state']['column']

        for i, row in enumerate(output):
            for j, column in enumerate(row):

                # If the first character of the set number is a letter that is not the line_id we are working on, discard the column
                if output[1][j] and output[1][j].strip()[0:1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', line['line_id']]:
                    continue

                if (column_offset == 0 and j not in [len(columns), len(columns) + 1]) or (column_offset > 0 and j not in [0, 1, len(columns), len(columns) + 1]):
                    selected_style = NORMAL_STYLE

                    if fonts[i][j]['bold'] and fonts[i][j]['italic']:
                        selected_style = BOLD_ITALIC_STYLE
                    if fonts[i][j]['bold']:
                        selected_style = BOLD_STYLE
                    if fonts[i][j]['italic']:
                        selected_style = ITALIC_STYLE


                    if time_regex.match(column):
                        time_values = time_regex.match(column).groups(0)
                        hour = int(time_values[0]) % 24
                        minute = int(time_values[2])
                        arrival_offset = time_values[1] if len(time_values[1]) == 1 else time_values[1].strip()

                        if time_values[3] == '14':
                            seconds = 15
                        elif time_values[3] == '12':
                            seconds  = 30
                        elif time_values[3] == '34':
                            seconds = 45
                        else:
                            seconds = 0

                        # The exact departure time in the WTT
                        departure_time = datetime(2015, 1, 1, hour, minute, seconds)
                        arrival_time = departure_time
                        if arrival_offset.strip():
                            arrival_time = departure_time - timedelta(seconds=linedata.ARRIVAL_OFFSETS[arrival_offset])

                        # Convert the departure and arrival datetimes to time (because you can't do timedelta on time)
                        departure_time = departure_time.time()
                        arrival_time = arrival_time.time()

                        # These are purely for the benefit of searching
                        departure_time_start = time(hour, minute)
                        if minute + 1 > 59:
                            departure_time_end = time((hour + 1) % 24, 0)
                        else:
                            departure_time_end = time(hour, minute + 1)

                        if rows[page_direction]['stations'].get(i):
                            servicepoints_query = session.query(
                                ServicePoint
                            ).filter_by(
                                station_id=rows[page_direction]['stations'][i],
                                line_id=line['line_id'],
                                direction=rows[page_direction]['direction']
                            )

                            possible_servicepoints = []
                            for point in servicepoints_query.all():
                                possible_servicepoints.append(point.id)

                            trips_query = session.query(
                                NewTimePoint
                            ).filter(
                                NewTimePoint.servicepoint_id.in_(possible_servicepoints)
                            ).filter(
                                NewTimePoint.departure.between(departure_time_start, departure_time_end)
                            )

                            # Complicated DOW running stuff
                            if page_day == linedata.WEEKDAYS and hour > 3:
                                trips_query = trips_query.filter_by(
                                    runs_monday=True
                                )
                            elif page_day == linedata.WEEKDAYS and hour < 3:
                                trips_query = trips_query.filter_by(
                                    runs_tuesday=True
                                )
                            elif page_day == linedata.SATURDAY and hour > 3:
                                trips_query = trips_query.filter_by(
                                    runs_saturday=True
                                )
                            elif page_day == linedata.SATURDAY and hour < 3:
                                trips_query = trips_query.filter_by(
                                    runs_sunday=True
                                )
                            elif page_day == linedata.SUNDAY and hour > 3:
                                trips_query = trips_query.filter_by(
                                    runs_sunday=True
                                )
                            elif page_day == linedata.SUNDAY and hour < 3:
                                trips_query = trips_query.filter_by(
                                    runs_monday=True
                                )

                            possible_trips = trips_query.all()

                            if len(possible_trips) == 1:
                                # Set the arrival/departure time to match the WTT
                                possible_trips[0].departure = departure_time

                                # If DB Arrival matches DB Departure, use WTT Arrival
                                if possible_trips[0].arrival == possible_trips[0].departure:
                                    possible_trips[0].arrival = arrival_time
                                # If DB Arrival does not exist, use WTT Arrival
                                elif possible_trips[0].arrival is None:
                                    possible_trips[0].arrival = arrival_time
                                # If DB Arrival does not equal DB Departure, and DB Arrival does not match WTT Arrival, use WTT arrival:
                                elif possible_trips[0].arrival != possible_trips[0].departure and possible_trips[0].arrival != arrival_time:
                                    possible_trips[0].arrival = arrival_time
                                else:
                                    # Change nothing
                                    pass

                                if not possible_trips[0].set_no and output[1][j]:
                                    set_no = re.search('(\d+)', output[1][j].strip()).group(0)
                                    trip_no = output[2][j]
                                    platform = None

                                    # Some lines contain NR headcodes in their set no data which matches the regex.
                                    if set_no and trip_no:
                                        time_point_query = session.query(
                                            NewTimePoint
                                        ).filter_by(
                                            trip=possible_trips[0].trip
                                        )

                                        for timepoint in time_point_query.all():
                                            timepoint.set_no = set_no
                                            timepoint.trip_no = trip_no

                                # Is this one with a platform in the sidebar?
                                if not possible_trips[0].platform and rows[page_direction]['platforms'].get(i) and isinstance(rows[page_direction]['platforms'][i], int):
                                    print possible_trips[0], rows[page_direction]['platforms'][i]
                                    possible_trips[0].platform = rows[page_direction]['platforms'][i]

                                session.commit()
                    else:
                        #### IMPORTANT - Currently won't do platforms for trains after midnight
                        #### Also double Edgware Roads won't work
                        #### This is for platforms specified on the main WTT. For those listed in the
                        #### sidebar, see above.
                        if rows[page_direction]['platforms'].get(i) and re.search('(\d+)', column.strip()):
                            servicepoints_query = session.query(
                                ServicePoint
                            ).filter_by(
                                station_id=rows[page_direction]['platforms'][i],
                                line_id=line['line_id'],
                                direction=rows[page_direction]['direction']
                            )

                            possible_servicepoints = []
                            for point in servicepoints_query.all():
                                possible_servicepoints.append(point.id)

                            if output[1][j].strip():
                                set_no = re.search('(\d+)', output[1][j].strip()).group(0)
                                trip_no = output[2][j]

                                if set_no and trip_no:

                                    trips_query = session.query(
                                        NewTimePoint
                                    ).filter(
                                        NewTimePoint.servicepoint_id.in_(possible_servicepoints)
                                    ).filter_by(
                                        set_no=set_no, trip_no=trip_no
                                    )

                                    # Complicated DOW running stuff
                                    if page_day == linedata.WEEKDAYS:
                                        trips_query = trips_query.filter_by(
                                            runs_tuesday=True
                                        )
                                    elif page_day == linedata.SATURDAY:
                                        trips_query = trips_query.filter_by(
                                            runs_saturday=True
                                        )
                                    elif page_day == linedata.SUNDAY:
                                        trips_query = trips_query.filter_by(
                                            runs_sunday=True
                                        )

                                    possible_trips = trips_query.all()

                                    if len(possible_trips) == 1 and re.match('(\d+)', column.strip()):
                                        if not possible_trips[0].platform:
                                            possible_trips[0].platform = column.strip()

                                            session.commit()

        variations[page_direction][page_day]['state']['column'] = j + column_offset + 1


# Then save all the spreadsheets
for variation in variations:
    for day in variations[variation]:
        if variations[variation][day]['state'].get('current_sheet', False):
            variations[variation][day]['output'].save('%s - %s - %s.xls' % (line_name, variation.title().replace('/', '-'), day.title()))
