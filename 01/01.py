#!/usr/bin/env python3

highest = 0

with open('input.txt', 'r') as f:
    current_elf = 0
    for line in f.readlines():
        if len(line.strip()) == 0:
            current_elf = 0
            continue
        current_elf += int(line)
        highest = max(current_elf, highest)
    highest = max(current_elf, highest)

print(highest)

