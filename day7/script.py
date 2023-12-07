#!/usr/bin/env python3

import os
import copy

workdir = os.getcwd()
inputfile = 'day7/input.txt'
cards = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def is_larger(card1: str, card2: str) -> bool:
    """ Returns true if card1 is larger than card2 """
    return (cards.index(card1) < cards.index(card2))

def eval_type(type: dict) -> str:
    """ Returns key of weakest card """
    weak = ''
    weak_key = ''
    for key in type:
        if weak == '': 
            weak = type[key]
            weak_key = key
            continue
        else:
            test_hand = type[key]
            for i in range(len(test_hand)):
                if test_hand[i] == weak[i]: continue
                if (is_larger(weak[i],test_hand[i])):
                    weak = test_hand
                    weak_key = key
                    break
                else:
                    break
    return weak_key 

def count_duplicates(s: str) -> list:
    char_count = {}
    list = []
    
    # Count each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for key in char_count:
        if char_count[key] > 1:
            list.append(char_count[key])
    
    return list

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

hands = [ line.split()[0] for line in data ]
bids = [ int(line.split()[1]) for line in data ]

five = {}
four = {}
full = {}
three = {}
two = {}
one = {}
high = {}

# Assign type for each hand
for index, hand in enumerate(hands):
    dup = count_duplicates(hand)
    # High card
    if len(dup) == 0:
        high[index] = hand
    # Five of a kind
    elif dup[0] == 5:
        five[index] = hand
    # Four of a kind
    elif dup[0] == 4:
        four[index] = hand
    # Full house
    elif len(dup) == 2 and max(dup) == 3 and min(dup) == 2:
        full[index] = hand
    # Three of a kind
    elif max(dup) == 3:
        three[index] = hand
    # Two pair
    elif len(dup) >= 2: 
        two[index] = hand
    # One pair
    elif dup[0] == 2:
        one[index] = hand

    

# Assign and evaluate rank

types = [high, one, two, three, full, four, five]

rank = 1
total_rank = 0
while rank <= len(data):
    for type in types:
        while len(type) > 0:
            if len(type) == 1:
                total_rank += bids[int(next(iter(type)))] * rank 
                print(bids[int(next(iter(type)))],rank)
                del type[next(iter(type))]
                rank += 1
                continue
            else:
                key = eval_type(type)
                total_rank += bids[int(key)] * rank
                print(bids[int(key)], rank)
                del type[key] 
                rank += 1
                continue

print(f'The total winnings are: {total_rank}.')



        
        




    
    

