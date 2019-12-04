from collections import Counter


PUZZLE_INPUT = "248345-746315"
low_end, high_end = [int(number) for number in PUZZLE_INPUT.split("-")]


"""
--- Part one ---
"""


def get_digit(number, n):
    return number // 10 ** n % 10


def two_adjacent(digits):
    prev = None
    for digit in digits:
        if prev is not None and prev == digit:
            return True
        prev = digit
    return False


def never_decrease(digits):
    prev = None
    for digit in digits:
        if prev is not None and prev < digit:
            return False
        prev = digit
    return True


def passwords_generator(low_end, high_end):
    for number in range(low_end, high_end + 1):
        digits = [get_digit(number, i) for i in range(len(str(number)))]
        if two_adjacent(digits) and never_decrease(digits):
            yield number


passwords = list(passwords_generator(low_end, high_end))
print(len(passwords))


"""
--- Part two ---
"""


def part_2_generator(passwords):
    for password in passwords:
        counts = Counter(str(password)).values()
        nr_of_pairs = len([val for val in counts if val == 2])
        if nr_of_pairs > 0:
            yield password


filtered_passwords = list(part_2_generator(passwords))
print(len(filtered_passwords))
