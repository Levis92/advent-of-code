# Day 6 - Tuning Trouble
# https://adventofcode.com/2022/day/6

# Format data
with open("data.txt") as f:
    buffer = f.read()


def find_marker_pos(char_count: int) -> int:
    for index in range(0, len(buffer)):
        if len(set(buffer[index: index + char_count])) == char_count:
            return index + char_count


# Part One
print(find_marker_pos(4))

# Part Two
print(find_marker_pos(14))
