def ys_path(data, you, san, path=[]):
    path = path + [you]
    if you == san:
        return path
    shortest = None
    for node in data[you]:
        if node not in path:
            new_path = ys_path(data, node, san, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


filename = "day6_data.txt"
data = {}
with open(filename) as file:
    for line in file.readlines():
        p, c = line.strip().split(')')
        if p not in data:
            data[p] = []
        if c not in data:
            data[c] = []
        data[p].append(c)
        data[c].append(p)
p = ys_path(data, 'YOU', 'SAN')
print('Answer 2:', len(p)-3)
