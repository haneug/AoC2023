#!/usr/bin/env python3

import os

workdir = os.getcwd()
inputfile = 'day5/example.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

def eval_map(block: list, things: list) -> list:
    name = block[0]
    #print(name)
    new_things = []
    map = {}
    # Read the map and create a dict
    for line in block:
        if 'map' in line: continue
        length = int(line.split()[2])
        source = int(line.split()[1])
        dest = int(line.split()[0])
        for thing in things:
            if source <= thing < source+length:
                diff = thing - source
                map[str(thing)] = dest + diff

    # things not on map just stay the same
    for thing in things:
        if str(thing) in map:
            new_things.append(map[str(thing)])
        else:
            new_things.append(thing)

    return new_things

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

# Generate range seeds
range_things = [] 
for i in range(0, len(things), 2):
    start, length = things[i], things[i+1]
    # Creating a range for each pair
    pair_range = list(range(start, start+length))
    for j in pair_range:
        range_things.append(j)


#Get the maps
current_block = []
for line in data:
    if line.strip() and line != data[-1]:
        current_block.append(line)
    else:
        things = eval_map(current_block, things)
        range_things = eval_map(current_block, range_things)
        current_block = []

print(f'The lowest location is {min(things)}.')
print(f'The lowest location for a range of seeds is {min(range_things)}.')

