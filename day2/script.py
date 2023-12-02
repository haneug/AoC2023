#!/usr/bin/env python3

import os
import copy

workdir = os.getcwd()
inputfile = 'day2/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()


def check_game(game: str) -> int:
    """ Return ID if game is valid and zero if not """

    reveals = game.split(':')[1].split(';')
    for reveal in reveals:
        virt_bag = copy.deepcopy(bag)
        rev_list = reveal.split(',')
        for rev in rev_list:
            number = int(rev.split()[0])
            color = rev.split()[1]
            virt_bag[color] -= number
        check = any(value < 0 for value in virt_bag.values())
        if check: return 0

    return int(game.split()[1].split(':')[0])

def check_bag(game: str) -> int:
    """ Return power of required bag in a game """

    reveals = game.split(':')[1].split(';')
    req_bag = {key: 0 for key in bag}
    for reveal in reveals:
        virt_bag = {key: 0 for key in bag}
        rev_list = reveal.split(',')
        for rev in rev_list:
            number = int(rev.split()[0])
            color = rev.split()[1]
            virt_bag[color] += number
        for key in req_bag:
            if key in virt_bag and virt_bag[key] > req_bag[key]:
                req_bag[key] = virt_bag[key]

    power = 1
    for key in req_bag:
        power *= req_bag[key]

    return power 

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum_id = 0
sum_power = 0
for game in data: 
    sum_id += check_game(game)
    sum_power += check_bag(game)

print(f'The sum of the valid game IDs is {sum_id}.')
print(f'The sum of the powers of required bags is {sum_power}.')