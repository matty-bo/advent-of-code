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
print("Station:", station)
tab = []
for i in range(0, len(p)):
    distance = abs(station[0] - p[i][0]) + abs(station[1] - p[i][1])
    a = math.atan2(station[1] - p[i][1], station[0] - p[i][0])
    if distance != 0:
        tab.append([p[i], distance, round(a, 3)])
q1_laser = []
q2, q3, q4 = [], [], []
for line in tab:
    if line[0][0] >= station[0] and line[0][1] <= station[1]:
        q1_laser.append([line[1], line[2]])
    if line[0][0] >= station[0] and line[0][1] > station[1]:
        q2.append([line[1], line[2]])
    if line[0][0] < station[0] and line[0][1] >= station[1]:
        q3.append([line[1], line[2]])
    if line[0][0] < station[0] and line[0][1] < station[1]:
        q4.append([line[1], line[2]])
q1_laser.sort(key=lambda laser_tab: (laser_tab[1], laser_tab[0]))
q2.sort(key=lambda q2: (q2[1], q2[0]))
q3.sort(key=lambda q3: (q3[1], q3[0]))
q4.sort(key=lambda q4: (q4[1], q4[0]))
q1_laser.extend(q2)
q1_laser.extend(q3)
q1_laser.extend(q4)
indexes = set()
for i in range(len(q1_laser)):
    if i < len(q1_laser) - 1:
        while q1_laser[i][1] == q1_laser[i + 1][1]:
            i += 1
    indexes.add(i+1)
que = []
beg = 0
for i in indexes:
    que.append(q1_laser[beg:i])
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