# Format data
with open("data.txt") as f:
    my_numbers = [int(i) for i in f.readlines()]

"""
--- Part One ---
"""
found_it = False
for i, n in enumerate(my_numbers):
    if found_it:
        break
    for m in my_numbers[i + 1 :]:
        if n + m == 2020:
            print(n * m)
            found_it = True
            break

"""
--- Part Two ---
"""
found_it = False
for i, n in enumerate(my_numbers):
    if found_it:
        break
    for j, m in enumerate(my_numbers[i + 1 :]):
        if found_it:
            break
        for k in my_numbers[i + j + 1 :]:
            if n + m + k == 2020:
                print(n * m * k)
                found_it = True
                break
