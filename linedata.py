# Tube directions
EASTBOUND = 'EASTBOUND'
WESTBOUND = 'WESTBOUND'
NORTHBOUND = 'NORTHBOUND'
SOUTHBOUND = 'SOUTHBOUND'
NORTHWESTBOUND = 'NORTH/WESTBOUND'
SOUTHEASTBOUND = 'SOUTH/EASTBOUND'

# Tube operating days
WEEKDAYS = 'MONDAYS TO FRIDAYS'
SATURDAY = 'SATURDAYS'
SUNDAY = 'SUNDAYS'

POSSIBLE_DAYS = [WEEKDAYS, SATURDAY, SUNDAY]

ARRIVAL_OFFSETS = {
    '+': 15,
    'a': 30,
    'A': 45,
    'b': 60,
    'B': 75,
    'c': 90,
    'C': 105,
    'd': 120,
    'D': 135,
    'e': 150,
    'E': 165,
    'f': 180,
    'F': 195,
    'g': 210,
    'G': 225,
    'h': 240,
    'H': 255,
    'j': 270,
    'J': 285,
    'k': 300,
    'K': 315,
    'l': 330,
    'L': 345,
}


# District
DISTRICT = {
    'line_name': 'District',
    'line_id': 'D',

    'variations': {
                    WESTBOUND:
                            {
                                WEEKDAYS: {'output': None, 'state': {}},
                                SATURDAY: {'output': None, 'state': {}},
                                SUNDAY  : {'output': None, 'state': {}}
                            },
                    EASTBOUND:
                            {
                                WEEKDAYS: {'output': None, 'state': {}},
                                SATURDAY: {'output': None, 'state': {}},
                                SUNDAY  : {'output': None, 'state': {}}
                            }
                },

    'columns': [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892],

    # Everything before this 'top' is header.
    'header': 108,

    # Everything before these are row names
    'row_names': [],

    'rows': { # Yes they are different, no, I don't understand why.
            WESTBOUND: {                  #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56
                            'rows'      : [108, 126, 144, 153, 161, 170, 178, 189, 198, 205, 213, 222, 231, 239, 248, 258, 266, 275, 284, 293, 301, 310, 318, 328, 337, 345, 354, 363, 371, 380, 387, 395, 404, 416, 425, 440, 450, 457, 465, 474, 482, 487, 500, 509, 520, 528, 537, 544, 553, 565, 571, 579, 584, 593, 602, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 543],
                            'stations': {
                                11: 'UPM',
                                12: 'DGE',
                                14: 'BKG',
                                15: 'PLW',
                                17: 'WHM',
                                18: 'WCL',
                                19: 'ALE',
                                20: 'LST',
                                22: 'ALD',
                                23: 'THL',
                                24: 'MAN',
                                25: 'EMB',
                                26: 'SKN',
                                28: 'GRD',
                                29: 'HST',
                                32: 'ERD',
                                34: 'HST',
                                36: 'ECT',
                                37: 'PGR',
                                38: 'PUT',
                                39: 'EPY',
                                40: 'WDN',
                                42: 'OLY',
                                44: 'WKN',
                                45: 'HMD',
                                46: 'TGR',
                                47: 'RMD',
                                49: 'ACT',
                                51: 'ECM',
                                52: 'EBY',
                            },
                            'platforms': {
                                9: 'UPM',
                                31: 'ERD',
                                33: 'HST',
                                35: 'ECT',
                                53: 'EBY',
                            },
                            'direction': 'W'
                        },
            EASTBOUND: {                  #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55
                            'rows'      : [108, 126, 144, 153, 161, 170, 178, 189, 198, 205, 213, 222, 231, 239, 248, 258, 266, 275, 284, 293, 301, 310, 318, 328, 337, 345, 354, 363, 371, 380, 387, 397, 407, 415, 422, 432, 440, 450, 457, 465, 477, 484, 493, 502, 509, 520, 528, 537, 544, 553, 565, 571, 579, 584, 593, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 543],
                            'stations': {
                                8: 'EBY',
                                10: 'ECM',
                                12: 'ACT',
                                14: 'RMD',
                                15: 'TGR',
                                16: 'HMD',
                                17: 'WKN',
                                19: 'OLY',
                                21: 'WDN',
                                22: 'EPY',
                                23: 'PUT',
                                24: 'PGR',
                                25: 'ECT',
                                28: 'HST',
                                30: 'ERD',
                                33: 'HST',
                                34: 'GRD',
                                35: 'SKN',
                                36: 'EMB',
                                37: 'MAN',
                                38: 'THL',
                                39: 'ALD',
                                41: 'LST',
                                42: 'ALE',
                                43: 'WCL',
                                44: 'WHM',
                                46: 'PLW',
                                47: 'BKG',
                                49: 'DGE',
                                50: 'UPM',
                            },
                            'platforms': {
                                7: 'EBY',
                                26: 'ECT',
                                29: 'HST',
                                31: 'ERD',
                                51: 'UPM',
                            },
                            'direction': 'E'
                        }
            }
}

# Jubilee
JUBILEE = {
    'line_name': 'Jubilee',
    'line_id': 'J',

    'variations': {
                    NORTHWESTBOUND:
                            {
                                WEEKDAYS: {'output': None, 'state': {}},
                                SATURDAY: {'output': None, 'state': {}},
                                SUNDAY  : {'output': None, 'state': {}}
                            },
                    SOUTHEASTBOUND:
                            {
                                WEEKDAYS: {'output': None, 'state': {}},
                                SATURDAY: {'output': None, 'state': {}},
                                SUNDAY  : {'output': None, 'state': {}}
                            }
                },

    'columns': [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892],

    # Everything before this 'top' is header.
    'header': 108,

    # Everything before these are row names
    'row_names': [],

    'rows': { # Yes they are different, no, I don't understand why.
            NORTHWESTBOUND: {             #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57
                            'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 258, 266, 275, 284, 293, 301, 310, 320, 328, 337, 345, 354, 363, 371, 380, 390, 399, 408, 416, 425, 434, 442, 451, 460, 470, 479, 487, 496, 505, 514, 522, 531, 540, 549, 560, 568, 576, 584, 593, 602, 610, 619, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 527],
                            'stations': {
                                10: 'SFD',
                                12: 'WHM',
                                14: 'CNT',
                                15: 'NGW',
                                17: 'CWF',
                                20: 'CWR',
                                21: 'BER',
                                22: 'LON',
                                24: 'SWK',
                                25: 'WLO',
                                26: 'WMS',
                                28: 'CHX',
                                29: 'GPK',
                                30: 'BDS',
                                31: 'BST',
                                33: 'SJW',
                                34: 'SWC',
                                36: 'FRD',
                                37: 'WHD',
                                39: 'KIL',
                                40: 'WLG',
                                41: 'DHL',
                                42: 'NEA',
                                44: 'WPK',
                                47: 'KBY',
                                48: 'QBY',
                                49: 'CPK',
                                51: 'STA',
                            },
                            'platforms': {
                                9: 'SFD',
                                16: 'NGW',
                                18: 'CWF',
                                35: 'FRD',
                                45: 'WPK',
                                52: 'STA',
                            },
                            'direction': 'N'
                        },
            SOUTHEASTBOUND: {             #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58
                            'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 622, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 527],
                            'stations': {
                                9: 'STA',
                                11: 'CPK',
                                12: 'QBY',
                                13: 'KBY',
                                16: 'WPK',
                                18: 'NEA',
                                19: 'DHL',
                                20: 'WLG',
                                21: 'KIL',
                                23: 'WHD',
                                24: 'FRD',
                                26: 'SWC',
                                27: 'SJW',
                                28: 'BST',
                                30: 'BDS',
                                31: 'GPK',
                                32: 'CHX',
                                34: 'WMS',
                                35: 'WLO',
                                37: 'SWK',
                                38: 'LON',
                                40: 'BER',
                                41: 'CWR',
                                42: 'CWF',
                                44: 'NGW',
                                47: 'CNT',
                                48: 'WHM',
                                51: 'SFD',
                            },
                            'platforms': {
                                8: 'STA',
                                15: 'WPK',
                                25: 'FRD',
                                43: 'CWF',
                                45: 'NGW',
                                52: 'SFD',
                            },
                            'direction': 'S'
                        }
            }
}

# NOT COMPLETE YET
METROPOLITAN = {
    'line_name': 'Metropolitan',
    'line_id': 'M',

    'variations': {
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
                },

    'columns': [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892],

    # Everything before this 'top' is header.
    'header': 108,

    # Everything before these are row names
    'row_names': [],

    'rows': {
                NORTHBOUND : {
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 636],
                                'nodashrows': [],
                                'tableoffsets':[0, 527]
                            },
                SOUTHBOUND : {
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 622, 636],
                                'nodashrows': [],
                                'tableoffsets':[0, 527]
                            }
            }
}

# Northern
NORTHERN = {
    'line_name': 'Northern',
    'line_id': 'N',

    'variations': {
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
                },

    'columns': [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892],

    # Everything before this 'top' is header.
    'header': 108,

    # Everything before these are row names
    'row_names': [],

    'rows': {
                NORTHBOUND : {                #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  57
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 554, 561, 570, 578, 587, 596, 608, 622, 636],
                                'nodashrows': [],
                                'tableoffsets':[0, 543],
                                'stations': {
                                    12: 'MOR',
                                    13: 'TBY',
                                    14: 'STK',
                                    15: 'KEN',
                                    16: 'KEN',
                                    18: 'CHX',
                                    19: 'TCR',
                                    20: 'EUS',
                                    21: 'MCR',
                                    23: 'LON',
                                    24: 'MGT',
                                    25: 'KXX',
                                    26: 'EUS',
                                    27: 'CTN',
                                    29: 'CTN',
                                    30: 'ARC',
                                    32: 'EFY',
                                    33: 'FYC',
                                    36: 'MHE',
                                    39: 'HBT',
                                    42: 'HMP',
                                    46: 'GGR',
                                    48: 'COL',
                                    50: 'EDG',
                                },
                                'platforms': {
                                    11: 'MOR',
                                    15: 3,
                                    16: 1,
                                    20: 1,
                                    26: 3,
                                    27: 1,
                                    29: 3,
                                    34: 'FYC',
                                    40: 'HBT',
                                    45: 'GGR',
                                    51: 'EDG',
                                },
                                'direction': 'N'
                            },
                SOUTHBOUND : {                #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  57
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 519, 528, 537, 546, 556, 563, 570, 578, 587, 596, 608, 622, 636],
                                'nodashrows': [],
                                'tableoffsets':[0, 543],
                                'stations': {
                                    9: 'EDG',
                                    11: 'COL',
                                    13: 'GGR',
                                    17: 'HMP',
                                    20: 'HBT',
                                    23: 'MHE',
                                    26: 'FYC',
                                    27: 'EFY',
                                    29: 'ARC',
                                    30: 'CTN',
                                    32: 'CTN',
                                    33: 'EUS',
                                    34: 'KXX',
                                    35: 'MGT',
                                    36: 'LON',
                                    38: 'MCR',
                                    39: 'EUS',
                                    40: 'TCR',
                                    41: 'CHX',
                                    43: 'KEN',
                                    44: 'KEN',
                                    45: 'STK',
                                    46: 'TBY',
                                    47: 'MOR',
                                },
                                'platforms': {
                                    8: 'EDG',
                                    14: 'GGR',
                                    19: 'HBT',
                                    25: 'FYC',
                                    30: 4,
                                    32: 2,
                                    33: 6,
                                    39: 2,
                                    43: 2,
                                    44: 4,
                                    48: 'MOR',
                                },
                                'direction': 'S'
                            }
            }
}


# Piccadilly
PICCADILLY = {
    'line_name': 'Piccadilly',
    'line_id': 'P',

    'variations': {
                    WESTBOUND:
                            {
                                WEEKDAYS: {'output': None, 'state': {}},
                                SATURDAY: {'output': None, 'state': {}},
                                SUNDAY  : {'output': None, 'state': {}}
                            },
                    EASTBOUND:
                            {
                                WEEKDAYS: {'output': None, 'state': {}},
                                SATURDAY: {'output': None, 'state': {}},
                                SUNDAY  : {'output': None, 'state': {}}
                            }
                },

    'columns': [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892],

    # Everything before this 'top' is header.
    'header': 108,

    # Everything before these are row names
    'row_names': [],

    'rows': {
                WESTBOUND : {
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 636],
                                'nodashrows': [],
                                'tableoffsets':[0, 527],
                                'stations': {
                                    8: 'CFS',
                                    10: 'OAK',
                                    12: 'AGR',
                                    15: 'WGN',
                                    16: 'FPK',
                                    17: 'KXX',
                                    18: 'HOL',
                                    19: 'GPK',
                                    20: 'HPC',
                                    21: 'KNB',
                                    23: 'ECT',
                                    24: 'HMD',
                                    26: 'TGR',
                                    27: 'ACT',
                                    30: 'NFD',
                                    33: 'BOS',
                                    34: 'OST',
                                    35: 'HNC',
                                    36: 'HTX',
                                    37: 'HRC',
                                    38: 'HTF',
                                    39: 'HRV',
                                    43: 'ECM',
                                    46: 'ALP',
                                    47: 'SHR',
                                    48: 'RLN',
                                    49: 'RUI',
                                    51: 'HDN',
                                    52: 'UXB',
                                },
                                'platforms': {
                                    7: 'CFS',
                                    11: 'AGR',
                                    25: 'HMD',
                                    28: 'ACT',
                                    31: 'NFD',
                                    53: 'UXB',
                                },
                                'direction': 'W'
                            },
                EASTBOUND : {
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 622, 636],
                                'nodashrows': [],
                                'tableoffsets':[0, 527],
                                'stations': {
                                    8: 'UXB',
                                    9: 'HDN',
                                    11: 'RUI',
                                    12: 'RLN',
                                    13: 'SHR',
                                    14: 'ALP',
                                    15: 'NEL',
                                    18: 'ECM',
                                    22: 'HRV',
                                    23: 'HTF',
                                    24: 'HRC',
                                    25: 'HTX',
                                    26: 'HNC',
                                    27: 'BOS',
                                    29: 'NFD',
                                    32: 'ACT',
                                    34: 'TGR',
                                    35: 'HMD',
                                    37: 'ECT',
                                    39: 'HPC',
                                    40: 'GPK',
                                    41: 'HOL',
                                    42: 'KXX',
                                    43: 'ARL',
                                    44: 'FPK',
                                    45: 'WGN',
                                    48: 'AGR',
                                    50: 'OAK',
                                    52: 'CFS',
                                },
                                'platforms': {
                                    7: 'UXB',
                                    30: 'NFD',
                                    33: 'ACT',
                                    36: 'HMD',
                                    49: 'AGR',
                                    53: 'CFS',
                                },
                                'direction': 'E'
                            }
            }
}

# Victoria
VICTORIA = {
    'line_name': 'Victoria',
    'line_id': 'V',

    'variations': {
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
                },

    'columns': [160, 198, 231, 263, 296, 328, 361, 393, 426, 458, 490, 523, 555, 588, 620, 653, 685, 718, 750, 782, 815, 892],

    # Everything before this 'top' is header.
    'header': 108,

    # Everything before these are row names
    'row_names': [],

    'rows': {
                NORTHBOUND : {                #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 270, 284, 292, 300, 309, 321, 330, 343, 352, 361, 373, 381, 387, 396, 405, 413, 422, 431, 443, 448, 465, 474, 482, 491, 500, 515, 525, 534, 540, 587, 596, 604],
                                'nodashrows': [],
                                'tableoffsets':[0, 551],
                                'stations': {
                                    15: 'BRX',
                                    16: 'STK',
                                    17: 'VUX',
                                    18: 'PIM',
                                    20: 'VIC',
                                    21: 'GPK',
                                    22: 'OXC',
                                    24: 'WST',
                                    25: 'EUS',
                                    26: 'KXX',
                                    29: 'HBY',
                                    30: 'FPK',
                                    33: 'SVS',
                                    40: 'TTH',
                                    41: 'BHR',
                                    42: 'WAL',
                                },
                                'platforms': {
                                    14: 'BRX',
                                    32: 'SVS',
                                    43: 'WAL',
                                },
                                'direction': 'N'
                            },
                SOUTHBOUND : {                #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47
                                'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 396, 405, 413, 422, 435, 448, 457, 465, 474, 486, 490, 505, 517, 526, 535, 544, 587, 596, 604],
                                'nodashrows': [],
                                'tableoffsets':[0, 551],
                                'stations': {
                                    16: 'WAL',
                                    17: 'BHR',
                                    18: 'TTH',
                                    26: 'SVS',
                                    29: 'FPK',
                                    30: 'HBY',
                                    32: 'KXX',
                                    33: 'EUS',
                                    34: 'WST',
                                    36: 'OXC',
                                    37: 'GPK',
                                    38: 'VIC',
                                    40: 'PIM',
                                    41: 'VUX',
                                    42: 'STK',
                                    43: 'BRX',
                                },
                                'platforms': {
                                    15: 'WAL',
                                    27: 'SVS',
                                    44: 'BRX',
                                },
                                'direction': 'S'
                            }
            }
}
