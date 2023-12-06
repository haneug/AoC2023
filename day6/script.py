#!/usr/bin/env python3

import os
import copy

workdir = os.getcwd()
inputfile = 'day6/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

def eval_race(time_limit: int, win_dist: int) -> int:
    wins = 0
    time = 0
    while time <= time_limit:
        dist = (time*(time_limit-time))
        if dist > win_dist: wins += 1
        time += 1
    return wins

times = [int(item) for item in data[0].split()[1:]]
distances = [int(item) for item in data[1].split()[1:]]

mult_wins = 1

for i in range(len(times)):
    mult_wins *= eval_race(times[i],distances[i])

print(f'The Multiplied number of possible winning conditions is: {mult_wins}.')