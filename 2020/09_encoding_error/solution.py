from itertools import combinations
from typing import List, Tuple

# Format data
with open("data.txt") as f:
    numbers = [int(n) for n in f.readlines()]


"""
--- Part One ---
"""


for i, n in enumerate(numbers[25:], start=25):
    sums = [m + k for m, k in combinations(numbers[i - 25 : i], 2)]
    if n not in sums:
        print(not_valid := n)
        break


"""
--- Part Two ---
"""


def get_seq(num_list: List[int]) -> Tuple[bool, List[int]]:
    num_sum, seq = 0, []
    for m in num_list:
        num_sum += m
        seq.append(m)
        if num_sum >= not_valid:
            return num_sum == not_valid, seq
    return False, seq


for i in range(len(numbers)):
    found_it, seq = get_seq(numbers[i:])
    if found_it:
        print(max(seq) + min(seq))
        break
