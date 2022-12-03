# Day 2 - Rock Paper Scissors
# https://adventofcode.com/2022/day/2

# Format data
with open("data.txt") as f:
    rounds = [round.strip().split(" ") for round in f.readlines()]


def calc_points(opponent: str, me: str) -> int:
    choice_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }[me]
    winner_points = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3,
    }[opponent + me]
    return choice_points + winner_points


# Part One
print(sum([calc_points(opponent, me) for (opponent, me) in rounds]))


# Part Two
def match_result(opponent: str, result: str) -> str:
    return {
        "X": {
            "A": "Z",
            "B": "X",
            "C": "Y"
        },
        "Y": {
            "A": "X",
            "B": "Y",
            "C": "Z"
        },
        "Z": {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }
    }[result][opponent]


print(
    sum([
        calc_points(opponent, match_result(opponent, result))
        for (opponent, result) in rounds
    ])
)
