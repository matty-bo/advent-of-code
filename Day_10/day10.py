import math

filename = "day10_data.txt"
data = []
with open(filename) as file:
    for line in file:
        data.append(list(line.strip()))
w = len(data[0])
h = len(data)
p = []
for j in range(0, h):
    for i in range(0, w):
        if data[j][i] == '#':
            p.append([i, j])
maxx = 0
ps = {}
for mp in p:
    angles = set()
    for op in p:
        if mp != op:
            a = math.atan2(mp[1] - op[1], mp[0] - op[0],)
            angles.add(a)
    ps[mp[0], mp[1]] = angles

maxx = max(len(ps[line]) for line in ps)

station = None
for line in ps:
    if len(ps[line]) == maxx:
        station = line
print("Task 1:", maxx)
print("Station:",station)

tab = []
for i in range(0, len(p)):
    distance = abs(station[0] - p[i][0]) + abs(station[1] - p[i][1])
    a = math.atan2(station[1] - p[i][1], station[0] - p[i][0])
    if distance != 0:
        tab.append([p[i], distance, round(a, 3)])

laser_tab = []
for line in tab:
    if line[0][0] >= station[0] and line[0][1] <= station[1]:
        laser_tab.append([line[1], line[2]])
new2 = []
for line in tab:
    if line[0][0] >= station[0] and line[0][1] > station[1]:
        new2.append([line[1], line[2]])
new3 = []
for line in tab:
    if line[0][0] < station[0] and line[0][1] >= station[1]:
        new3.append([line[1], line[2]])
new4 = []
for line in tab:
    if line[0][0] < station[0] and line[0][1] < station[1]:
        new4.append([line[1], line[2]])

laser_tab.sort(key=lambda laser_tab: (laser_tab[1], laser_tab[0]))
new2.sort(key=lambda new2: (new2[1], new2[0]))
new3.sort(key=lambda new3: (new3[1], new3[0]))
new4.sort(key=lambda new4: (new4[1], new4[0]))
laser_tab.extend(new2)
laser_tab.extend(new3)
laser_tab.extend(new4)

indexes = set()
for i in range(len(laser_tab)):
    if i < len(laser_tab) - 1:
        while laser_tab[i][1] == laser_tab[i + 1][1]:
            i += 1
    indexes.add(i+1)

que = []
beg = 0
for i in indexes:
    que.append(laser_tab[beg:i])
    beg = i

j = 0
count = 0
dist_slope = None
destroy = 200
while count != destroy:
    if count == destroy - 1:
        dist_slope = que[j].copy()
    if que[j]:
        que[j].pop(0)
        count += 1
    j += 1
    if j >= len(que):
        j = 0
dist_slope = dist_slope[0]
ans2 = None
for p in tab:
    if dist_slope[0] == p[1] and dist_slope[1] == p[2]:
        ans2 = p[0]
print("Task 2: (%d, %d)" % (ans2[0], ans2[1]))