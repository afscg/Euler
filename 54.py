#!/usr/bin/env python3

value_char = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def score(encoded):
    ''' (rank, rank_val, v4, v3, v2, v1) '''
    suits = set([e[1] for e in encoded])
    values = sorted([value_char[e[0]] for e in encoded], reverse=True)

    consecutive = True
    for i in range(len(values) - 1):
        if values[i] - values[i + 1] != 1:
            consecutive = False
            break

    if len(suits) == 1 and consecutive:
        # Straight/Royal flush.
        return [8, values[0]]

    if values[0] == values[3]:
        # Four of a kind at front.
        return [7, values[0], values[4]]

    if values[1] == values[4]:
        # Four of a kind at back.
        return [7, values[1], values[0]]

    if values[0] == values[2] and values[3] == values[4]:
        # Full house at front.
        return [6, values[0], values[3]]

    if values[0] == values[1] and values[2] == values[4]:
        # Full house at back.
        return [6, values[2], values[0]]

    if len(suits) == 1:
        # Flush.
        return [5] + values

    if consecutive:
        # Straight.
        return [4, values[0]]

    if values[0] == values[2]:
        # Three of a kind at 0.
        return [3, values[0], values[3], values[4]]

    if values[1] == values[3]:
        # Three of a kind at 1.
        return [3, values[1], values[0], values[4]]

    if values[2] == values[4]:
        # Three of a kind at 2.
        return [3, values[2], values[0], values[1]]

    # Find pairs and singles.
    singles = []
    pairs = []
    i = 0
    while i < len(values):
        if i + 1 < len(values) and values[i] == values[i + 1]:
            pairs.append(values[i])
            i += 2
        else:
            singles.append(values[i])
            i += 1

    return [len(pairs)] + pairs + singles

wins = 0
with open('data/54.txt') as f:
    for ln in f:
        tokens = ln.split()
        if score(tokens[:5]) > score(tokens[5:]):
            wins += 1
print(wins)
