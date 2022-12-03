# Day 3 - Rucksack Reorganization
# https://adventofcode.com/2022/day/3
from functools import reduce
from typing import List

# Format data
with open("data.txt") as f:
    rucksacks = f.read().split("\n")


def find_common_char(*strings: List[str]) -> str:
    common_chars = reduce(lambda all, curr: set(all) & set(curr), strings)
    return "".join(list(common_chars))


def get_priority(char: str) -> int:
    return ord(char) - (ord("a") - 1 if char.islower() else ord("A") - 27)


# Part One
def split_in_half(string: str) -> List[str]:
    n = len(string)
    string1 = string[0:n//2]
    string2 = string[n//2:]
    return string1, string2


def calc_priority(string: str) -> int:
    strings = split_in_half(string)
    char = find_common_char(*strings)
    return get_priority(char)


print(sum([calc_priority(rucksack) for rucksack in rucksacks]))

# Part Two
chunk_size = 3
chunked_list = [
    rucksacks[i:i+chunk_size] for i in range(0, len(rucksacks), chunk_size)
]


def calc_priority_part_two(strings: List[str]) -> int:
    char = find_common_char(*strings)
    return get_priority(char)


print(sum([calc_priority_part_two(group) for group in chunked_list]))
