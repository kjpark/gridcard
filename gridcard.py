#!/usr/bin/env python3

import string
import re

from config import *

gridcard = [A, B, C, D, E, F, G, H, I, J]

def help():
    print('\nvalid syntax is case-insensitive and includes:')
    print(  '\t[D3][G2][A2]' + 
          '\n\t[A2] [I5] [A1]' +
          '\n\ta1 b2 c3' +
          '\n\tD4E5F5' +
          '\n\tE2] [H1] [H4 \t# partial entries containing all essential info OK')

def gridcard_error(message, idx, val):
    print('\nERR: Gridcard Format' +
          '\nMSG: {}'.format(message) +
          '\nSRC: {} = {}'.format(string.ascii_uppercase[idx], val))

def validate_gridcard():
    column_regex = re.compile('^[A-Za-z0-9]{5}$')
    results = []
    for idx, val in enumerate(gridcard):
        if type(val) != str:
            gridcard_error('column not a string, check `config.py`', idx, val)
            results.append(False)
            break
        elif not re.match(column_regex, val):
            gridcard_error('invalid pattern, check `config.py`', idx, val)
            results.append(False)
            break
        else:
            results.append(True)

    return True if all(results) else False    

def input_error(message, input):
    print('\nERR: Bad Input' +
          '\nMSG: {}\n'.format(message) +
          '\n IN: {}'.format(input) +
          '\n RE: ^([A-J][0-5])+$')
    help()

def process_input():
    input_regex = re.compile('^([A-J][0-5])+$')
    coords = input('\ninput code:\n\n  -->\t').upper()
    coords = ''.join(char for char in coords if char.isalnum())

    if re.match(input_regex, coords):
        # split into a list of coords ie 'H1A2C4' -> ['H1', 'A2', 'C4']
        n = 2
        coords = [coords[i:i+n] for i in range(0, len(coords), n)]
        return coords
    else:
        input_error('input fails to match regex', coords)
        return False

def translate(coords):
    result = ''

    for coord in coords:
        x = string.ascii_uppercase.index(coord[0])
        y = int(coord[1]) - 1 # lists start at 0
        result += gridcard[x][y]

    print('\n  IN:\t' + ' '.join(coords))
    print('\n OUT:\t' + result)

def main():
    if validate_gridcard():
        input = process_input()
        if input:
            translate(input)

if __name__ == '__main__':
    main()
