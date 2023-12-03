#!/usr/bin/env python3

import os
import numpy as np

workdir = os.getcwd()
inputfile = 'day3/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()


def is_symbol(symbol: str) -> bool:
    """ Checks if the string is not alphanumeric or a period """
    return not symbol.isalnum() and symbol != '.'

def check_index(pos: tuple[int, int], schem : np.ndarray) -> bool:
    """ Checks if a special character is adjacent to a position """
    x = pos[0]
    y = pos[1]
    shape = schem.shape
    x_max = shape[0]
    y_max = shape[1]
    # Now we have to go through all combinations
    for xstep in [-1, 0, 1]:
        for ystep in [-1, 0, 1]:
            xpos = x + xstep
            ypos = y + ystep
            # Check if position is valid
            if (0 <= xpos < x_max) and (0 <= ypos < y_max):
                # Check if there is a symbol for this position
                if is_symbol(str(schem[xpos][ypos])):
                    return True
  
    return False


def get_parts(schem: np.ndarray) -> int:
    """ Finds all the parts and returns their sum """
    sum = 0
    cnum = ''
    index_list = []
    is_valid = False
    for index, element in np.ndenumerate(schem):
        if element.isdigit():
            cnum += element
            index_list.append(index)
        else:
            if cnum != '':
                # we found the number now we have to check it
                for pos in index_list: 
                    is_valid = check_index(pos,schem)
                    #print(cnum, index_list)
                    if is_valid:
                        #print('valid: ' + cnum)
                        sum += int(cnum)
                        break
                # reset number and list
                cnum = ''
                index_list = []

    return sum

# Convert input to an 2D array
schematic = np.full((len(data),len(data[0])), fill_value=' ', dtype='<U1')

for i, line in enumerate(data):
    schematic[i, :len(line)] = list(line)

sum_part = 0
sum_part = get_parts(schematic)

print(f'The sum of the valid parts is {sum_part}.')