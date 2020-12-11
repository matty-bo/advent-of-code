def empty_prim(i, j, data):
    for way in adj:
        n = nn(i, j, way, data)
        if n == '#':
            return 'L'
    return '#'


def occup_prim(i, j, data):
    count = 0
    for way in adj:
        n = nn(i, j, way, data)
        count += n == '#'
        if count >= 5:
            return 'L'
    return '#'


def outside(i, j, data):
    li, ui = 0, len(data)
    lj, uj = 0, len(data[0])
    return not (li <= i < ui and lj <= j < uj)


# look for nearest neighbour which isn't floor
def nn(i, j, way, data):
    while True:
        i, j = adj[way](i, j)
        if outside(i, j, data):
            return False
        if data[i][j] != '.':
            break
    return data[i][j]


def get_changes(data):
    changes = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_val = data[i][j]
            if data[i][j] == 'L':
                new_val = empty_prim(i, j, data)
            elif data[i][j] == '#':
                new_val = occup_prim(i, j, data)
            if new_val != data[i][j]:
                changes[(i, j)] = new_val
    return changes


def apply_changes(changes, data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in changes:
                data[i][j] = changes[(i, j)]
    return data


filename = 'input11.txt'
with open(filename) as file:
    data = [[seat for seat in x] for x in file.read().splitlines()]

adj = {0: lambda i, j: (i - 1, j - 1),  # 0 3 6
       1: lambda i, j: (i - 1, j),  # 1 4 7
       2: lambda i, j: (i - 1, j + 1),  # 2 5 8
       3: lambda i, j: (i, j - 1),
       5: lambda i, j: (i, j + 1),
       6: lambda i, j: (i + 1, j - 1),
       7: lambda i, j: (i + 1, j),
       8: lambda i, j: (i + 1, j + 1)}

changes = {1: 1}
while len(changes) != 0:
    changes = get_changes(data)
    data = apply_changes(changes, data)

ans1 = sum(data[i][j] == '#' for i in range(len(data)) for j in range(len(data[0])))
print('Answer 1:', ans1)
