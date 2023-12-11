#!/usr/bin/env python3

import os
import math

workdir = os.getcwd()
inputfile = 'day8/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

def check_point(point: str, target: str) -> bool:
    if target in point[-len(target):]:
        return True
    else:
        return False

def get_steps(point: str, target: str) -> int:
    steps = 0
    iter = 0
    while not check_point(point, target):
        direct = inst[iter]
        if direct == 'L': 
            point = map[point][0]
        elif direct == 'R':
            point = map[point][1]
        iter += 1
        iter = iter % len(inst)
        steps += 1
    return steps

inst = data.pop(0)
data.pop(0)

map = {}

for line in data:
    name = line.split()[0]
    entry = line.split('=')[1].strip("() ").split(', ')
    map[name] = entry


point = 'AAA'
goal = 'ZZZ'

#steps = get_steps(point, goal)

#print(f'The total number of steps is: {steps}.')

### Part two ###

points = []
steps = 0
iter = 0
goal = 'Z'
paths = []

# find start points
for key in map:
    if key[-1] == 'A':
        points.append(key)

for point in points:
    steps = 0
    steps = get_steps(point, goal)
    paths.append(steps)

steps = math.lcm(*paths)
print(f'The total number of steps for ghosts is: {steps}.')