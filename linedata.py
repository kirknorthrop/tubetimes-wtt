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

# Jubilee
JUBILEE = {
    'line_name': 'Jubilee',

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
                            }
                        },
            SOUTHEASTBOUND: {             #  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58
                            'rows'      : [108, 126, 144, 153, 161, 179, 187, 196, 205, 213, 222, 231, 239, 248, 257, 265, 274, 283, 292, 300, 309, 318, 326, 335, 343, 352, 361, 369, 378, 387, 396, 405, 413, 422, 431, 439, 448, 457, 465, 474, 482, 491, 500, 509, 517, 526, 535, 544, 552, 561, 570, 578, 587, 596, 604, 613, 622, 636],
                            'nodashrows': [],
                            'tableoffsets':[0, 527]
                        }
            }
}

METROPOLITAN = {
    'line_name': 'Metropolitan',

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