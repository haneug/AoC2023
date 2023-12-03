#!/usr/bin/env python3

import os
import numpy as np

workdir = os.getcwd()
inputfile = 'day3/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

### Part one functions ###

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

### Part two functions ###


def check_number(xpos: int, ypos: int, schem : np.ndarray) -> tuple[int, int, int]:
    """ returns the whole number and its start coordinates """
    start = ypos
    number = ''
    # find the start of the digit
    while start > 0:
        if schem[xpos,start-1].isdigit():
            start -= 1
            continue
        break
    # find the digit
    iter = start
    while iter < schem.shape[1]:
        if schem[xpos,iter].isdigit():
            number += str(schem[xpos,iter])
            iter +=1
            continue
        break
    return xpos, start, int(number)


def get_numb(pos: tuple[int, int], schem : np.ndarray) -> int:
    """ Returns the gear ratio """
    numbers = {}
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
                # Check whether it is a number and assign it to a dict
                if schem[xpos][ypos].isdigit():
                    tuple_num = check_number(xpos,ypos,schem)
                    #print(tuple_num)
                    numbers[str(tuple_num[0]) + ' ' + str(tuple_num[1])] = tuple_num[2]
    
    if len(numbers) == 2:
        ratio = 1
        for number in numbers.values():
            ratio *= number
    else:
        ratio = 0

    return ratio


def get_gears(schem: np.ndarray) -> int:
    """ Finds all the gears and returns the sum of their ratios """
    sum = 0
    for index, element in np.ndenumerate(schem):
        if element == '*':
            gears = get_numb(index,schem)
            sum += gears
    return sum


# Convert input to an 2D array
schematic = np.full((len(data),len(data[0])), fill_value=' ', dtype='<U1')

for i, line in enumerate(data):
    schematic[i, :len(line)] = list(line)

### Part one ###
sum_part = 0
sum_part = get_parts(schematic)

print(f'The sum of the valid parts is {sum_part}.')

### Part two ###
sum_gear = 0
sum_gear = get_gears(schematic)

print(f'The sum of the gear ratios is {sum_gear}.')

