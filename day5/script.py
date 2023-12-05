#!/usr/bin/env python3

import os
import copy

workdir = os.getcwd()
inputfile = 'day5/input.txt'

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
    
    #print('single: ', new_things)
    return new_things

def eval_map_pairs(block: list, things: list) -> list:
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
        for i in range(0, len(things), 2):
            # find the overlap
            overlap_start = max(source,things[i])
            overlap_end = min(source+length-1,things[i]+things[i+1]-1)
            # if they overlap
            if overlap_start < overlap_end:
                # append overlap to new_things 
                new_things.append(overlap_start-source+dest)
                new_things.append(overlap_end-overlap_start+1)
                # Split old range 
                # Case 0: Remove complete overlap
                if things[i] == overlap_start and things[i]+things[i+1]-1 == overlap_end:
                    things[i] = 'NaN'
                    things[i+1] = 'NaN'
                    continue
                # Case 1: Overlap is in the middle of things
                elif things[i] < overlap_start and things[i]+things[i+1] > overlap_end:
                    # split into two ranges
                    things.append(overlap_end)
                    things.append(things[i]+things[i+1]-1-overlap_end)
                    things[i+1] = overlap_start - things[i] + 1
                    continue
                # Case 2: Overlap is at the start of things
                elif things[i] == overlap_start:
                    things[i+1] += (things[i]-overlap_end) - 1
                    things[i] = overlap_end + 1
                    continue
                # Case 3: Overlap is at the end of things
                elif (things[i] + things[i+1]) == overlap_end:
                    things[i+1] = overlap_start-things[i] + 1
                    continue
            # No overlap
            else:
                continue

        filtered_things = [item for item in things if item != 'NaN']
        things = filtered_things
 

    # things not on map just stay the same
    for thing in things:
        new_things.append(thing)
    #print('pair: ', new_things)
    return new_things



# Get the seeds
things = [int(item) for item in data.pop(0).split()[1:]]
pair_things = copy.deepcopy(things)
data.pop(0)

# Generate range seeds - too much for real input only testing!
#range_things = [] 
#for i in range(0, len(things), 2):
#    start, length = things[i], things[i+1]
#    # Creating a range for each pair
#    pair_range = list(range(start, start+length))
#    for j in pair_range:
#        range_things.append(j)


#Get the maps
current_block = []
for line in data:
    if line.strip() and line != data[-1]:
        current_block.append(line)
    else:
        #things = eval_map(current_block, things)
        #range_things = eval_map(current_block, range_things)
        pair_things = eval_map_pairs(current_block, pair_things)
        current_block = []

print(f'The lowest location is {min(things)}.')
#print(f'The lowest location for a range of seeds is {min(range_things)}.')
print(f'The lowest location for a range of seeds (evaluated with pairs) is {min(pair_things[::2])}.')

