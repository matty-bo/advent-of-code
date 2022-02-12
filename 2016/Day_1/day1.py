with open('input1.txt') as file:
    data = [line for line in file.read().strip().split(', ')]
steps = [(line[0], int(line[1:])) for line in data]

rotate = {'R': {'U': 'R' , 'R': 'D', 'D': 'L' , 'L': 'U'},
          'L': {'U': 'L' , 'L': 'D', 'D': 'R' , 'R': 'U'}}
journey = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
orientation = 'U'

for r, d in steps:
    orientation = rotate[r][orientation]
    journey[orientation] += d
ans1 = abs(journey['U'] - journey['D']) + abs(journey['R'] - journey['L'])
print('Answer 1:', ans1)

points = []
move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
x, y = 0, 0
ans2 = -1
for r, d in steps:
    orientation = rotate[r][orientation]
    for i in range(d):
        x += move[orientation][0]
        y += move[orientation][1]
        if (x, y) in points:
            ans2 = abs(x) + abs(y)
            break
        else:
            points.append((x, y))
        if ans2 != -1:
            break
print('Answer 2:', ans2)