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
    if len(group) == 1:
        return len(group[0])
    total = 0
    for l in group[0]:
        is_present = True
        for g in group[1:]:
            if l not in g:
                is_present = False
        if is_present:
            total += 1
    return total


print(sum(count_group(g) for g in group_answers))
