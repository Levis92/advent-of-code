# Format data
from enum import Enum
from dataclasses import dataclass


class PositionKey(str, Enum):
    MIN = "min_pos"
    MAX = "max_pos"


@dataclass
class Policy:
    password: str
    letter: str
    min_pos: int
    max_pos: int


def format_data(line: str) -> Policy:
    rule, password = line.strip().split(": ")
    rule_range, letter = rule.split(" ")
    min_pos, max_pos = [int(n) for n in rule_range.split("-")]
    return Policy(password, letter, min_pos, max_pos)


with open("data.txt") as f:
    my_policies = [format_data(line) for line in f.readlines()]


"""
--- Part One ---
"""


def matches_count_policy(pol: Policy) -> bool:
    return pol.min_pos <= pol.password.count(pol.letter) <= pol.max_pos


is_valid_count = sum(1 for pol in my_policies if matches_count_policy(pol))

print(is_valid_count)

"""
--- Part Two ---
"""


def has_letter(data: Policy, key: PositionKey) -> bool:
    return data.password[getattr(data, key.value) - 1] == data.letter


def matches_position_policy(pol: Policy) -> bool:
    in_first_pos = has_letter(pol, PositionKey.MIN)
    in_second_pos = has_letter(pol, PositionKey.MAX)
    return (in_first_pos or in_second_pos) and not (in_first_pos and in_second_pos)


is_valid_count = sum(1 for pol in my_policies if matches_position_policy(pol))

print(is_valid_count)
