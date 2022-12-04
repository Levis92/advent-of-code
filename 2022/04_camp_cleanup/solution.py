# Day 4 - Camp Cleanup
# https://adventofcode.com/2022/day/4
from typing import List, Set
from dataclasses import dataclass

# Format data
with open("data.txt") as f:
    def format_range(range_val: str) -> List[int]:
        return [int(val) for val in range_val.split("-")]

    assignment_pairs = [
        [format_range(val) for val in pair.strip().split(",")]
        for pair in f.readlines()
    ]


@dataclass
class Assignment:
    start: int
    end: int

    def fully_overlaps(self, assignment: "Assignment") -> bool:
        self_interval = get_range_set(self)
        compare_interval = get_range_set(assignment)
        return (
            len(self_interval - compare_interval) == 0
            or len(compare_interval - self_interval) == 0
        )

    def overlaps(self, assignment: "Assignment") -> bool:
        self_interval = get_range_set(self)
        compare_interval = get_range_set(assignment)
        return (
            len(self_interval - compare_interval) < len(self_interval)
            or len(compare_interval - self_interval) < len(compare_interval)
        )


def get_range_set(assignment: Assignment) -> Set[int]:
    return set(range(assignment.start, assignment.end + 1))


fully_overlap_count = 0
overlap_count = 0

for elf1, elf2 in assignment_pairs:
    fully_overlaps = Assignment(*elf1).fully_overlaps(Assignment(*elf2))
    overlaps = Assignment(*elf1).overlaps(Assignment(*elf2))

    if fully_overlaps:
        fully_overlap_count = fully_overlap_count + 1

    if overlaps:
        overlap_count = overlap_count + 1

# Part One
print(fully_overlap_count)
# Part Two
print(overlap_count)
