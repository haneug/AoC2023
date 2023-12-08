#!/usr/bin/env python3

import os

workdir = os.getcwd()
inputfile = 'day8/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

inst = data.pop(0)
data.pop(0)

map = {}

for line in data:
    name = line.split()[0]
    entry = line.split('=')[1].strip("() ").split(', ')
    map[name] = entry

steps = 0
point = 'AAA'
iter = 0

while point != 'ZZZ':
    direct = inst[iter]
    if direct == 'L': 
        point = map[point][0]
    elif direct == 'R':
        point = map[point][1]
    iter += 1
    iter = iter % len(inst)
    steps += 1

print(f'The total number of steps is: {steps}.')
