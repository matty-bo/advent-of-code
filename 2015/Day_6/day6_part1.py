import re


filename = 'day6_data.txt'
dirty_data = []
with open(filename) as file:
    for line in file:
        dirty_data.append(line.strip('\n'))
adj_data = {'off': 0,
            'on': 1,
            'toggle': 2}

data = []
for row in dirty_data:
    row = re.split('\\s|,', row)
    try:
        row.remove('through')
        row.remove('turn')
    except:
        pass
    row[0] = adj_data.get(row[0], row[0])
    data.append(list(map(int, row)))


grid = [[0 for i in range(1000)] for j in range(1000)]
for row in data:
    if row[0] == 0 or row[0] == 1:
        for i in range(row[1], row[3]+1):
            for j in range(row[2], row[4]+1):
                grid[i][j] = row[0]
    elif row[0] == 2:
        for i in range(row[1], row[3]+1):
            for j in range(row[2], row[4]+1):
                grid[i][j] = int(not grid[i][j])
ans1 = 0
for i in range(1000):
    for j in range(1000):
        ans1 += grid[i][j]
print('Answer 1:', ans1)
