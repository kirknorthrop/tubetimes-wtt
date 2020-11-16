# -*- coding: utf-8 -*-
#!/usr/bin/python

# London Underground Working Timetable PDF converter
#
# Copyright (c) 2013-2020 Kirk Northrop <kirk@krn.me.uk>
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
import csv
import re
import sys

from bs4 import BeautifulSoup
from xlwt import Workbook, easyxf

import linedata

# Default styles for Tube WTTs
NORMAL_STYLE = easyxf("font: height 140;")
BOLD_STYLE = easyxf("font: height 140, bold true;")
ITALIC_STYLE = easyxf("font: height 140, italic true;")
BOLD_ITALIC_STYLE = easyxf("font: height 140, bold true, italic true;")

TIME_REGEX = re.compile("(\d\d)(\s*[A-Za-z+ ]\s*)(\d\d)(\d\d)?")
STRIP_TAGS_REGEX = re.compile("(.*?)<.+?>(.*?)</.+>(.*?)")


### SET LINE HERE
line = linedata.METROPOLITAN


line_name = line["line_name"]
days = line["days"]
directions = line["directions"]
columns = line["columns"]
header = line["header"]
row_names = line["row_names"]
rows = line["rows"]

# So we need to create workbooks for all the variations
variations = {}
for direction in directions:
    variations[direction] = {}
    for day in days:
        variations[direction][day] = {
            "output": [],
            "state": {
                "number_of_rows": len(rows[direction]["rows"]),
                "current_column": 0,
            },
        }

# Get the xml and create the soup
f = open(sys.argv[1], "r")
print("Creating soup...")
soup = BeautifulSoup(f, "lxml")

lefts = {}

# Then for each page...
for page in soup.pdf2xml.find_all("page"):

    print("Processing page " + page["number"])

    page_direction = None
    page_day = None

    # So we want to look in the header and find out which direction/day this is.
    possible_directions = rows.keys()
    for text in page.find_all("text"):
        if int(text["top"]) < header:
            for direction in possible_directions:
                if direction in text.renderContents().decode("utf-8"):
                    page_direction = direction
                    break
            for day in days:
                if day in text.renderContents().decode("utf-8"):
                    page_day = day
                    break

    if page_direction and page_day:
        output = [
            [
                ""
                for _ in range(len(columns * len(rows[page_direction]["tableoffsets"])))
            ]
            for _ in range(
                len(rows[page_direction]["rows"])
                * len(rows[page_direction]["tableoffsets"])
            )
        ]
        fonts = [
            [
                {"bold": False, "italic": False}
                for _ in range(len(columns * len(rows[page_direction]["tableoffsets"])))
            ]
            for _ in range(
                len(rows[page_direction]["rows"])
                * len(rows[page_direction]["tableoffsets"])
            )
        ]

        # So for as many tables as we have...
        for offset_index, offset in enumerate(rows[page_direction]["tableoffsets"]):
            for text in page.find_all("text"):
                row_no = None
                col_no = None

                for i, col in enumerate(columns):
                    if int(text["left"]) < col:
                        col_no = i + (len(columns) * offset_index)
                        break

                for i, row in enumerate(rows[page_direction]["rows"]):
                    if (
                        int(text["top"]) < (row + offset)
                        and int(text["top"])
                        < (
                            rows[page_direction]["rows"][
                                len(rows[page_direction]["rows"]) - 1
                            ]
                            + offset
                        )
                        and int(text["top"])
                        > (rows[page_direction]["rows"][0] + offset)
                    ):
                        row_no = i
                        break

                if row_no is not None and col_no is not None:
                    cell_value = text.renderContents().decode("utf-8").strip()

                    if text.find_all(True):
                        cell_value = STRIP_TAGS_REGEX.sub(
                            "\g<1>\g<2>\g<3>", cell_value
                        ).strip()

                        if cell_value:
                            if len(text.find_all("b")):
                                fonts[row_no][col_no]["bold"] = True
                            if len(text.find_all("i")):
                                fonts[row_no][col_no]["italic"] = True

                    if row_no is not None and col_no is not None and cell_value:
                        output[row_no][col_no] += str(cell_value)

            for i, row in enumerate(output):
                for column in row:
                    if TIME_REGEX.match(column):
                        time_values = TIME_REGEX.match(column).groups(0)

                        detail_letter = (
                            time_values[1]
                            if len(time_values[1]) == 1
                            else time_values[1].strip()
                        )
                        column = time_values[0] + detail_letter + time_values[2]

                        if time_values[3] == "14":
                            column += "¼"
                        elif time_values[3] == "12":
                            column += "½"
                        elif time_values[3] == "34":
                            column += "¾"

        # if (
        #     variations[page_direction][page_day]["state"].get("column", None) is None
        #     or (
        #         variations[page_direction][page_day]["state"].get("column")
        #         + len(output[0])
        #     )
        #     > 255
        # ):
        #     ws = variations[page_direction][page_day]["output"].add_sheet(
        #         "Page " + page["number"]
        #     )
        #     # variations[page_direction][page_day]["state"]["current_sheet"] = ws
        #     column_offset = 0
        # # else:
        # # ws = variations[page_direction][page_day]["state"]["current_sheet"]
        # column_offset = variations[page_direction][page_day]["state"]["column"]

        column_offset = 0

        for i, row in enumerate(output):
            for j, column in enumerate(row):

                if (
                    column_offset == 0 and j not in [len(columns), len(columns) + 1]
                ) or (
                    column_offset > 0
                    and j not in [0, 1, len(columns), len(columns) + 1]
                ):
                    selected_style = NORMAL_STYLE

                    if fonts[i][j]["bold"] and fonts[i][j]["italic"]:
                        selected_style = BOLD_ITALIC_STYLE
                    if fonts[i][j]["bold"]:
                        selected_style = BOLD_STYLE
                    if fonts[i][j]["italic"]:
                        selected_style = ITALIC_STYLE

                    if TIME_REGEX.match(column):
                        time_values = TIME_REGEX.match(column).groups(0)

                        detail_letter = (
                            time_values[1]
                            if len(time_values[1]) == 1
                            else time_values[1].strip()
                        )
                        val = time_values[0] + detail_letter + time_values[2]

                        if time_values[3] == "14":
                            val += "¼"
                        elif time_values[3] == "12":
                            val += "½"
                        elif time_values[3] == "34":
                            val += "¾"

                        output[i][j] = val
                        # ws.write(i, j + column_offset, val, selected_style)
                    else:
                        pass
                        # ws.write(i, j + column_offset, column, selected_style)

        variations[page_direction][page_day]["state"]["column"] = j + column_offset + 1
        if variations[page_direction][page_day]["output"]:
            for i, row in enumerate(output):
                variations[page_direction][page_day]["output"][i] += row

        else:
            variations[page_direction][page_day]["output"] = output


# Then save all the spreadsheets
for variation in variations:
    for day in variations[variation]:
        file_name = (
            f"{line_name} - {variation.title().replace('/', '-')} - {day.title()}.csv"
        )

        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(variations[variation][day]["output"])
