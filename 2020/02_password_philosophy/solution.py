# Format data
def format_data(data: str):
    rule, password = data.split(": ")
    rule_range, letter = rule.split(" ")
    min_allowed, max_allowed = [int(i) for i in rule_range.split("-")]
    return {
        "password": password.strip(),
        "letter": letter,
        "min_allowed": min_allowed,
        "max_allowed": max_allowed,
    }


with open("data.txt") as f:
    my_data = [format_data(i) for i in f.readlines()]


"""
--- Part One ---
"""
is_valid = 0
for pg in my_data:
    nr_present = sum(1 for c in pg["password"] if c == pg["letter"])
    if pg["min_allowed"] <= nr_present <= pg["max_allowed"]:
        is_valid += 1

print(is_valid)

"""
--- Part Two ---
"""


def is_present(data: dict, key: str) -> bool:
    try:
        return data["password"][data[key] - 1] == data["letter"]
    except:
        return False


is_valid = 0
for pg in my_data:
    is_first_position = is_present(pg, "min_allowed")
    is_second_position = is_present(pg, "max_allowed")
    if (is_first_position or is_second_position) and not (
        is_first_position and is_second_position
    ):
        is_valid += 1

print(is_valid)
