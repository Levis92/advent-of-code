# Format data
from typing import List
from functools import lru_cache


with open("data.txt") as f:
    adapters = [int(l) for l in f.readlines()]


"""
--- Part One ---
"""

current_joltage = 0
adapters_copy = [*adapters]
diff_3_count = 1
diff_1_count = 0

while len(adapters_copy) > 0:
    lowest = min(adapters_copy)
    adapters_copy.remove(lowest)
    diff = lowest - current_joltage
    current_joltage = lowest
    if diff == 3:
        diff_3_count += 1
    elif diff == 1:
        diff_1_count += 1


print(diff_1_count * diff_3_count)


"""
--- Part Two ---
"""
from math import prod

current_joltage = 0
adapters_copy = [*adapters]
adapters_copy.sort()
combinations_count = []


def solve(adapters: List[int], prev: int, prev_array: List[int], combs: List[int]):
    global combinations_count
    adapters_copy = [*adapters][:3]
    loop = [n for n in adapters_copy if n - prev <= 3]
    for a in loop:
        count = len(loop)
        adapters_copy.remove(a)
        if len(adapters_copy) == 0:
            combinations_count.append(prod([*combs, count]))
            break
        solve(adapters_copy, a, [*prev_array, a], [*combs, count])


solve(adapters_copy, 0, [], [])


def can_plug(next_joltage, current_joltage):
    return next_joltage - current_joltage <= 3


target = max(adapters) + 3


@lru_cache
def combinations(idx=0, joltage=0):
    if idx == len(adapters):
        return can_plug(target, joltage)

    total = combinations(idx + 1, joltage)
    if can_plug(adapters[idx], joltage):
        total += combinations(idx + 1, adapters[idx])
    return total


print(combinations())
