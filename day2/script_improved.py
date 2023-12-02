#!/usr/bin/env python3

import os
import copy

workdir = os.getcwd()
inputfile = 'day2/input.txt'

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()


def check_game(game: str) -> (int, int):
    """ 
    Return ID if game is valid and zero if not. 
    Return power of required bag in a game.
    """

    ID = int(game.split()[1].split(':')[0])
    reveals = game.split(':')[1].split(';')
    req_bag = {key: 0 for key in bag}
    for reveal in reveals:
        virt_bag = copy.deepcopy(bag)
        rev_list = reveal.split(',')
        for rev in rev_list:
            number = int(rev.split()[0])
            color = rev.split()[1]
            virt_bag[color] -= number
        check = any(value < 0 for value in virt_bag.values())
        if check: ID = 0
        for key in req_bag:
            if key in virt_bag and (-(virt_bag[key]-bag[key])) > req_bag[key]:
                req_bag[key] = (-(virt_bag[key]-bag[key]))
    
    power = 1
    for key in req_bag:
        power *= req_bag[key]

    return ID, power

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum_id = 0
sum_power = 0
for game in data: 
    result = check_game(game)
    sum_id += result[0]
    sum_power += result[1]

print(f'The sum of the valid game IDs is {sum_id}.')
print(f'The sum of the powers of required bags is {sum_power}.')