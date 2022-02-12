from itertools import product


def get_neighbours(point):
    neighbours = list(product([-1, 0, 1], repeat=len(point)))
    neighbours.remove(tuple(0 for _ in range(len(point))))
    neighbours = [tuple(point[dim] + n[dim]
                        for dim in range(len(point)))
                  for n in neighbours]
    return neighbours


def get_expanded_dim(dim):
    expanded_dim = {}
    for point, state in dim.items():
        neighbours = get_neighbours(point)
        neighbours = {n: '.' for n in neighbours if n not in dim}
        expanded_dim.update(neighbours)
    expanded_dim.update(dim)
    return expanded_dim


def get_next_cube_state(state, point, dim):
    neighbours = get_neighbours(point)
    active_count = 0
    for n in neighbours:
        if n in dim:
            active_count += dim[n] == '#'
    if state == '#':
        return '#' if active_count in [2, 3] else '.'
    elif state == '.':
        return '#' if active_count == 3 else '.'
    return -1, -1


def get_next_dim(dim):
    dim = get_expanded_dim(dim)
    next_states = {}
    for point, state in dim.items():
        next_cube_state = get_next_cube_state(state, point, dim)
        next_states[point] = next_cube_state
    dim.update(next_states)
    return dim


filename = 'input17.txt'
with open(filename) as file:
    data = file.read()
data = [[cube for cube in row] for row in data.split('\n')]
dim_3d = {(x, y, 0): data[x][y] for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == '#'}
dim_4d = {(x, y, 0, 0): data[x][y] for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == '#'}

for i in range(6):
    dim_3d = get_next_dim(dim_3d)
ans1 = sum(cube_state == '#' for cube_state in dim_3d.values())
print('Answer 1:', ans1)

for i in range(6):
    dim_4d = get_next_dim(dim_4d)
ans2 = sum(cube_state == '#' for cube_state in dim_4d.values())
print('Answer 2:', ans2)
