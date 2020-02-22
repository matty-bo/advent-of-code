import re


filename = 'day6_data.txt'
dirty_data = []
with open(filename) as file:
    for line in file:
        dirty_data.append(line.strip('\n'))
adj_data = {'off': -1,
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
    for i in range(row[1], row[3]+1):
        for j in range(row[2], row[4]+1):
            grid[i][j] += row[0]
            if grid[i][j] < 0:
                grid[i][j] = 0
ans2 = 0
for i in range(1000):
    for j in range(1000):
        ans2 += grid[i][j]
print('Answer 2:', ans2)
