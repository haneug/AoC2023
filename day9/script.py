#!/usr/bin/env python3

import os
import copy

workdir = os.getcwd()
inputfile = 'day9/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

def get_extra(line: list) -> list:
    diff = []
    for i in range(0, len(line)-1):
        diff.append(int(line[i+1])-int(line[i]))
    return diff

sum_history = 0
sum_prev_history = 0

for line in data:
    list = [[int(item) for item in line.split()]]
    while any(item != 0 for item in list[-1]):
        list.append(get_extra(list[-1]))
    history = 0
    prev_history = 0
    for item in list:
        history += item[-1]
    rev_list = list[::-1]
    for i in range(0, len(rev_list)-1):
        prev_history = rev_list[i+1][0] - prev_history  
    sum_history += history
    sum_prev_history += prev_history

print(f'The sum of all histories is: {sum_history}.')
print(f'The sum of all the previous histories is: {sum_prev_history}.')

