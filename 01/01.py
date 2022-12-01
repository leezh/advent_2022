#!/usr/bin/env python3

elves = [0]

with open('input.txt', 'r') as f:
    for line in f.readlines():
        if len(line.strip(" \n\t")) == 0:
            elves.append(0)
            continue
        elves[-1] += int(line)

ranking = sorted(elves, reverse=True)

print(f'The elf with most snacks was carrying {ranking[0]} calories')
print(f'The top three elves with most snacks were carrying {sum(ranking[0:3])} calories total')
