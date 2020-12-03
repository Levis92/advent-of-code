# Format data
with open("data.txt") as f:
    grid = [[n for n in i if n != "\n"] for i in f.readlines()]

grid_width = len(grid[0])
grid_height = len(grid)


def go_down_slope(d_x: int, d_y: int):
    x, y, nr_of_trees = 0, 0, 0
    while (y := y + d_y) < grid_height:
        x = nx if (nx := x + d_x) < grid_width else nx - grid_width
        if grid[y][x] == "#":
            nr_of_trees += 1
    return nr_of_trees


"""
--- Part One ---
"""
print(go_down_slope(3, 1))


"""
--- Part Two ---
"""
from math import prod

tree_sums = (
    go_down_slope(d_x, d_y) for d_x, d_y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
)
print(prod(tree_sums))
