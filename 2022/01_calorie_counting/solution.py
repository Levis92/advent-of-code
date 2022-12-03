# Day 1 - Calorie Counting
# https://adventofcode.com/2022/day/1
from heapq import nlargest

# Format data
with open("data.txt") as f:
    elf_calorie_lists = [
        [int(calories) for calories in list.split("\n")]
        for list in f.read().split("\n\n")
    ]

total_calories_list = [sum(list) for list in elf_calorie_lists]

# Part One
print(max(total_calories_list))

# Part Two
print(sum(nlargest(3, total_calories_list)))
