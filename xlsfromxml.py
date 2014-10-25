# -*- coding: utf-8 -*-
#!/usr/bin/python

# London Underground Working Timetable Spreadsheet converter
# Created as part of the tubetimes project at http://tubetim.es/
#
# Copyright (c) 2014 Kirk Northrop <kirk@krn.me.uk>
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
from xlwt import Workbook, easyxf

# Default styles for Tube WTTs
NORMAL_STYLE = easyxf('font: height 140;')
BOLD_STYLE = easyxf('font: height 140, bold true;')
ITALIC_STYLE = easyxf('font: height 140, italic true;')
BOLD_ITALIC_STYLE = easyxf('font: height 140, bold true, italic true;')

# Tube directions
EASTBOUND = 'EASTBOUND'
WESTBOUND = 'WESTBOUND'
NORTHBOUND = 'NORTHBOUND'
SOUTHBOUND = 'SOUTHBOUND'

# Tube operating days
WEEKDAYS = 'MONDAYS TO FRIDAYS'
SATURDAY = 'SATURDAYS'
SUNDAY = 'SUNDAYS'

POSSIBLE_DAYS = [WEEKDAYS, SATURDAY, SUNDAY]

# LINE SPECIFIC - Metropolitan
line_name = 'Metropolitan'

variations = {
				NORTHBOUND:
						{
							WEEKDAYS: {'output': None, 'state': {}},
				 			SATURDAY: {'output': None, 'state': {}},
				 			SUNDAY  : {'output': None, 'state': {}}
						},
				SOUTHBOUND:
						{
							WEEKDAYS: {'output': None, 'state': {}},
							SATURDAY: {'output': None, 'state': {}},
							SUNDAY  : {'output': None, 'state': {}}								
						}
			}

columns = [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892]

# Everything before this 'top' is header.
header = 108

# Everything before these are row names
row_names = []

rows = {
			NORTHBOUND : {
							'rows'		: [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 636],
							'nodashrows': [],
							'tableoffsets':[0, 527]
						},
			SOUTHBOUND : {
							'rows'		: [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 622, 636],
							'nodashrows': [],
							'tableoffsets':[0, 527]
						}
		}


time_regex = re.compile('(\d\d)(\s*[A-Za-z ]\s*)(\d\d)(\d\d)?')
strip_tags_regex = re.compile('(.*?)<.+?>(.*?)</.+>(.*?)')


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
			for day in POSSIBLE_DAYS:
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

			for row in output:
				for column in row:
					if time_regex.match(column):
						time_values = time_regex.match(column).groups(0)
						
						detail_letter = time_values[1] if len(time_values[1]) == 1 else time_values[1].strip()
						column = time_values[0] + detail_letter + time_values[2]

						if time_values[3] == '14':
							column += u'¼'
						elif time_values[3] == '12':
							column += u'½'
						elif time_values[3] == '34':
							column += u'¾'

		if variations[page_direction][page_day]['state'].get('column', None) is None or (variations[page_direction][page_day]['state'].get('column') + len(output[0])) > 255:
			ws = variations[page_direction][page_day]['output'].add_sheet('Page ' + page['number'])
			variations[page_direction][page_day]['state']['current_sheet'] = ws
			column_offset = 0
		else:
			ws = variations[page_direction][page_day]['state']['current_sheet']
			column_offset = variations[page_direction][page_day]['state']['column']
		
		for i, row in enumerate(output):
			for j, column in enumerate(row):

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
						
						detail_letter = time_values[1] if len(time_values[1]) == 1 else time_values[1].strip()
						val = time_values[0] + detail_letter + time_values[2]

						if time_values[3] == '14':
							val += u'¼'
						elif time_values[3] == '12':
							val += u'½'
						elif time_values[3] == '34':
							val += u'¾'
			
						ws.write(i, j + column_offset, val, selected_style)
					else:
						ws.write(i, j + column_offset, column, selected_style)

		variations[page_direction][page_day]['state']['column'] = j + column_offset + 1


# Then save all the spreadsheets
for variation in variations:
	for day in variations[variation]:
		variations[variation][day]['output'].save('%s - %s - %s.xls' % (line_name, variation.title(), day.title()))
