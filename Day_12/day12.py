import copy
import re
import math

class Moon:
    def __init__(self, px, py, pz):
        self.p = [px, py, pz]
        self.v = [0, 0, 0]
    def __str__(self):
        return "<x=%d, y=%d, z=%d> <x=%d, y=%d, z=%d>" %\
               (self.p[0], self.p[1], self.p[2], self.v[0], self.v[1], self.v[2])
    def velocity(self):
        for i in range(0, 3):
            self.p[i] += self.v[i]

def gravity(moons):
    for i in range(0, 4):
        for j in range(i+1, 4):
            for k in range(0, 3):
                if moons[i].p[k] > moons[j].p[k]:   # update x
                    moons[i].v[k] -= 1
                    moons[j].v[k] += 1
                elif moons[i].p[k] < moons[j].p[k]:
                    moons[i].v[k] += 1
                    moons[j].v[k] -= 1

def cycle(moons, tps, tvs, i):
    count = 0
    origin = True
    while origin:
        p, v = [], []
        gravity(moons)
        for m in moons:
            m.velocity()
            p.append(m.p[i])
            v.append(m.v[i])
        count += 1
        if p == tps and v == tvs:
            origin = False
    return count

def lcm(a, b):
    return a*b // math.gcd(a, b)

filename = "day12_data.txt"
with open(filename) as file:
    data = file.read().splitlines()
for i in range(0, len(data)):
    data[i] = re.sub('.=', '', data[i][1:-1]).split(',')
for i in range(0, len(data)):
    data[i] = [int(j) for j in data[i]]
moons = []
for m in data:
    m = Moon(m[0], m[1], m[2])
    moons.append(m)
moons_copies = []
for i in range(0, 3):
    moons_copies.append(copy.deepcopy(moons))
for i in range(0, 1000):
    gravity(moons)
    for m in moons:
        m.velocity()
energy = 0
for m in moons:
    energy += (abs(m.p[0]) + abs(m.p[1]) + abs(m.p[2])) * (abs(m.v[0]) + abs(m.v[1]) + abs(m.v[2]))
print("Task 1:", energy)
c = []
for i in range(0, 3):
    paxis = [data[0][i], data[1][i], data[2][i], data[3][i]]
    vaxis = [0, 0, 0, 0]
    c.append(cycle(moons_copies[i], paxis, vaxis, i))
print("Task 2:", lcm(lcm(c[0], c[1]), c[2]))