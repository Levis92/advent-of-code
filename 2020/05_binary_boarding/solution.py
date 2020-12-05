# Format data
with open("data.txt") as f:
    seats = (l.strip() for l in f.readlines())

"""
--- Part One ---
"""
from typing import Tuple

row_range = (0, 127)
column_range = (0, 7)


def get_lower_half(start: int, end: int) -> Tuple[int, int]:
    return (start, end - (end - start + 1) / 2)


def get_upper_half(start: int, end: int) -> Tuple[int, int]:
    return (start + (end - start + 1) / 2, end)


def get_pos(seat_steps: str, _range: Tuple[int, int]) -> int:
    for step in seat_steps:
        if step in "FL":
            _range = get_lower_half(*_range)
        if step in "BR":
            _range = get_upper_half(*_range)
    return int(_range[0])


def get_seat_id(seat: str) -> int:
    row_steps, column_steps = seat[:7], seat[7:]
    row = get_pos(row_steps, row_range)
    column = get_pos(column_steps, column_range)
    return row * 8 + column


seat_ids = [get_seat_id(seat) for seat in seats]
print(max(seat_ids))


"""
--- Part Two ---
"""
for seat_id in range(min(seat_ids), max(seat_ids)):
    if seat_id not in seat_ids:
        print(seat_id)
