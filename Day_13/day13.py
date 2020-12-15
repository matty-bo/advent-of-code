def equ(r1, d1, r2, d2):
    i = 0
    while True:
        new_r = r1 + d1 * i
        new_div = d1 * d2
        if new_r % d2 == r2 % d2:
            return new_r, new_div
        i += 1


filename = 'input13.txt'
with open(filename) as file:
    timestamp = int(file.readline())
    data = file.read().split(',')

buses = [int(bus) for bus in data if bus != 'x']
departures = {timestamp + bus - timestamp % bus: bus
              for bus in buses}
departure = min(departures)
bus_id = departures[departure]
ans1 = (departure - timestamp) * bus_id
print('Answer 1:', ans1)

bus_deps = {int(data[i]): i for i in range(len(data)) if data[i] != 'x'}
y = list(bus_deps.values())
n = list(bus_deps)

r, d = y[0], n[0]
for i in range(1, len(y)):
    r, d = equ(r, d, y[i], n[i])
ans2 = d - r
print('Answer 2:', ans2)
