#!/usr/bin/env python3

import string

"""
#
# 1. SETUP
#

for each column, enter values from top to bottom

ex:
    | A | B | ...
    --------- ...
| 1 | H | W | ...
| 2 | 3 | 0 | ... ----> A = 'H3110'
| 3 | 1 | R | ...       B = 'W0RLD'
| 4 | 1 | L | ...       ...
| 5 | 0 | D | ...
    --------- ...

#
# 2. USE
#

`python3 gridcard.py`

"""

#
# EDIT THIS
#

A = ''
B = ''
C = ''
D = ''
E = ''
F = ''
G = ''
H = ''
I = ''
J = ''

#
# NO MORE EDITS REQD
#

gridcard = [A, B, C, D, E, F, G, H, I, J]

def validate_gridcard():
    results = []
    for idx, val in enumerate(gridcard):
        if type(val) != str:
            print('\nERR: each gridcard column must be a string')
            print('SRC: {} = {}'
                .format(string.ascii_uppercase[idx], val))
            results.append(False)
            break
        elif val.__len__() != 5:
            print('\nERR: each gridcard column must be 5 chars long')
            print('SRC: {} = \'{}\''
                .format(string.ascii_uppercase[idx], val))
            results.append(False)
            break
        else:
            results.append(True)

    return True if all(results) else False    

def help():
    print('\nvalid syntax includes:')
    print('\'a1 b2 c3\' OR \'D4 E5 F5\'')

def process_input():
    input_ok = []
    coords = input('\ninput code, lowercase ok:\n\n  -->\t').upper().split()

    for idx, coord in enumerate(coords):
        if coord.__len__() != 2:
            print('\nERR: {} is not 2 chars long'.format(coords[idx]))
            input_ok.append(False)
        elif coord[0] not in string.ascii_uppercase:
            print('\nERR: {} first char must be letter'.format(coords[idx]))
            input_ok.append(False)
        elif coord[0] not in string.ascii_uppercase[0:10]:
            print('\nERR: {} in {} is not between A-J'.format(coord[0], coord))
            input_ok.append(False)
        elif coord[1] not in string.digits:
            print('\nERR: {} second char must be a number'.format(coords[idx]))
            input_ok.append(False)
        elif int(coord[1]) not in range(1, 6):
            print('\nERR: {} in {} is not between 1-5'.format(coord[1], coord))
            input_ok.append(False)
        else:
            input_ok.append(True)
    
    return coords if all(input_ok) else False

def translate(coords):
    result = ''

    for coord in coords:
            x = string.ascii_uppercase.index(coord[0])
            y = int(coord[1]) - 1 # lists start at 0
            result += gridcard[x][y]

    print('\n  IN:\t' + ' '.join(coords))
    print('\n OUT:\t' + result)

def main():
    input = process_input()
    if validate_gridcard() and input:
        translate(input)
    else:
        help()

if __name__ == '__main__':
    main()
