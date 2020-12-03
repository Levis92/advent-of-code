from itertools import combinations

# Format data
with open("data.txt") as f:
    my_numbers = [int(i) for i in f.readlines()]

"""
--- Part One ---
"""
for n, m in combinations(my_numbers, 2):
    if n + m == 2020:
        print(n * m)
        break


"""
--- Part Two ---
"""
for n, m, k in combinations(my_numbers, 3):
    if n + m + k == 2020:
        print(n * m * k)
        break
