import re
from itertools import product
from typing import Set, Tuple

# Format data
with open("data.txt") as f:
    data = f.readlines()

"""
--- Part One ---
"""


def get_bag_color(line: str) -> str:
    return " ".join(line.split()[:2])


bags = set(
    get_bag_color(line)
    for line in data
    if re.search("contain .* shiny gold bags?", line)
)


def find_bags(bags: Set[str]) -> Set[str]:
    new_bags = set(
        get_bag_color(line)
        for line, bag in product(data, bags)
        if re.search(f"contain.*{bag}.*", line)
    )
    if len(bags | new_bags) == len(bags):
        return bags
    bags = bags | new_bags
    return bags | find_bags(bags)


print(len(find_bags(bags)))


"""
--- Part Two ---
"""


def format_match(match: str) -> Tuple[int, str]:
    count, *rest = match.split()
    return (int(count), " ".join(rest))


def count_bags(target_bag: str, count: int = 1) -> int:
    for line in data:
        if re.search(f"^{target_bag}", line):
            matches = [format_match(m) for m in re.findall("\d+ \w+ \w+", line)]

            if matches:
                return count + sum([count * count_bags(t, c) for c, t in matches])

    return count


print(count_bags("shiny gold bags") - 1)
