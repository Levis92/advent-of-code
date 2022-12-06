# Day 5 - Supply Stacks
# https://adventofcode.com/2022/day/5
from collections import defaultdict
from copy import deepcopy
from typing import List

# Format data
with open("data.txt") as f:
    crates, instructions = f.read().split("\n\n")
    crates = [[*row] for row in crates.split("\n")]
    crates.reverse()
    crate_stacks = defaultdict(lambda: [])
    for (column_index, char) in enumerate(crates[0]):
        if char.isnumeric():
            for row_index in range(1, len(crates)):
                crate = crates[row_index][column_index]
                if crate.isalpha():
                    crate_stacks[int(char)].append(crate)
    part_two_stacks = deepcopy(crate_stacks)
    instructions = instructions.split("\n")


def get_n_last(n: int, array: List[str]) -> List[str]:
    return array[-n:]


def get_all_exept_n_last(n: int, array: List[str]) -> List[str]:
    return array[:len(array) - n]


for instruction in instructions:
    _move, _from, _to = [
        int(string) for string in instruction.split(" ")
        if string.isnumeric()
    ]
    for _ in range(0, _move):
        crate = crate_stacks[_from].pop()
        crate_stacks[_to].append(crate)

    moved_crates = get_n_last(_move, part_two_stacks[_from])
    part_two_stacks[_from] = \
        get_all_exept_n_last(_move, part_two_stacks[_from])
    part_two_stacks[_to] = [*part_two_stacks[_to], *moved_crates]


def get_top_crates(stacks):
    return "".join([
        stack.pop() for stack_nr in range(1, len(stacks) + 1)
        if len(stack := stacks[stack_nr]) > 0
    ])


# Part One
print(get_top_crates(crate_stacks))
# Part Two
print(get_top_crates(part_two_stacks))
