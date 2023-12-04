#!/usr/bin/env python3

import os

workdir = os.getcwd()
inputfile = 'day4/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

sum_points = 0

for card in data:
    card_points = 0
    card_num = card.split(':')[0].split()[1]
    win_num = card.split(':')[1].split('|')[0].split()
    my_num = card.split(':')[1].split('|')[1].split()
    for num in my_num:
        if num in win_num:
            if card_points == 0:
                card_points += 1
            else:
                card_points *= 2
    sum_points += card_points

print(f'The sum of the card points is {sum_points}.')

    