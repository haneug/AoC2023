#!/usr/bin/env python3

import os

workdir = os.getcwd()
inputfile = 'day5/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

def eval_map(block: list, things: list) -> list:
    name = block.pop(0)
    print(name)
    new_things = []
    map = {}
    # Read the map and create a dict
    for line in block:
        length = int(line.split()[2])
        source = int(line.split()[1])
        dest = int(line.split()[0])
        for thing in things:
            if source <= thing <= source+length:
                diff = thing - source
                map[str(thing)] = dest + diff

    # things not on map just stay the same
    for thing in things:
        if str(thing) in map:
            new_things.append(map[str(thing)])
        else:
            new_things.append(thing)

    return new_things

# Get the seeds
things = [int(item) for item in data.pop(0).split()[1:]]
data.pop(0)

#Get the maps
current_block = []
for line in data:
    if line.strip() and line != data[-1]:
        current_block.append(line)
    else:
        things = eval_map(current_block, things)
        current_block = []

print(f'The lowest location is {min(things)}.')

