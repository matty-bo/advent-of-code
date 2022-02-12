from itertools import permutations


def distance(way):
    dist_sum = 0
    for i in range(len(way)-1):
        dist_sum += int(data.get((way[i], way[i+1]), None))
    return dist_sum


filename = 'day9_data.txt'
data = {}
with open(filename) as file:
    for line in file:
        row = line.strip().replace(' to ', ' ').replace(' = ', ',')
        c, dist = row.split(',')
        (c1, c2) = c.split()
        data[(c1, c2)] = dist
        data[(c2, c1)] = dist

cities = set()
for line in data:
    cities.add(line[0])
    cities.add(line[1])
cities = [c for c in cities]
ways = permutations(cities)
distances = [distance(perm) for perm in ways]
ans1, ans2 = min(distances), max(distances)
print("Answer 1:", ans1)
print("Answer 2:", ans2)
