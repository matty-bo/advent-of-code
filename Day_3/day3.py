filename = 'day3_data.txt'
with open(filename) as file:
    data = file.read()

moves = {'<': (-1, 0),
         '>': (1, 0),
         'v': (0, -1),
         '^': (0, 1)}
pos = (0, 0)
visited = set(pos)

for m in data:
    point = moves.get(m)
    pos = (pos[0]+point[0], pos[1]+point[1])
    visited.add(pos)
print('Answer 1:', len(visited))

srp = [(0, 0), (0, 0)]
visited = set()
for i in range(0, len(data)):
    point = moves.get(data[i])
    srp[i % 2] = (srp[i % 2][0]+point[0], srp[i % 2][1]+point[1])
    visited.add(srp[i % 2])

print('Answer 2:', len(visited))
