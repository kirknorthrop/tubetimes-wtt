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


# Jubilee - Needs more stations
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
                            'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 258, 266, 275, 284, 293, 301, 310, 320, 328, 337, 345, 354, 363, 371, 380, 390, 399, 408, 416, 425, 434, 442, 451, 460, 470, 479, 487, 496, 505, 514, 522, 531, 540, 549, 557, 566, 576, 584, 593, 602, 610, 619, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 527],
                            'stations': {
                                10: 'SFD'
                            },
                            'direction': 'N'
                        },
            SOUTHEASTBOUND: {             #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58
                            'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 622, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 527],
                            'stations': {
                                9: 'STA',
                                16: 'WPK'
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