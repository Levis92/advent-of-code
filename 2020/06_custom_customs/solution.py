# Format data
with open("data.txt") as f:
    data = f.read()


"""
--- Part One ---
"""
group_answers = [set(g.replace("\n", "")) for g in data.split("\n\n")]
print(sum(len(g) for g in group_answers))

"""
--- Part Two ---
"""
from typing import List

group_answers = [g.split("\n") for g in data.split("\n\n")]


def count_group(group: List[str]) -> int:
    return sum(1 for l in group[0] if "".join(group).count(l) == len(group))


print(sum(count_group(g) for g in group_answers))
