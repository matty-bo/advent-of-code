import re
from copy import deepcopy


def change_light(rows, columns, grid):
    state = grid[rows][columns]
    neighbours = 0
    for r in range(rows-1, rows+2):
        for c in range(columns-1, columns+2):
            if grid[r][c] == 1:
                neighbours += 1
    if state == 1:
        neighbours -= 1
        if neighbours not in [2, 3]:
            return 0
    elif state == 0:
        if neighbours == 3:
            return 1
    return state


def next_grid(grid):
    new_grid = deepcopy(grid)
    for r in range(1, rows+1):
        for c in range(1, columns+1):
            new_grid[r][c] = change_light(r, c, grid)
    return new_grid


filename = 'day18_data.txt'
with open(filename) as file:
    data = file.read()
data = re.sub('#', '1', data)
data = re.sub('\\.', '0', data).split('\n')
grid = [list(map(int, line)) for line in data]
rows, columns = 100, 100
ring = 0
for row in grid:
    row.insert(0, ring)
    row.append(ring)
grid.insert(0, [ring for i in grid[0]])
grid.append([ring for i in grid[0]])
for i in range(100):
    grid = next_grid(grid)
ans1 = 0
for row in grid:
    for light in row:
        ans1 += light
print('Answer 1:', ans1)
