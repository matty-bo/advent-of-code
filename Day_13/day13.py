import re
from itertools import permutations


def happiness(h_dict, perm):
    res = 0
    for i in range(len(perm)-1):
        res += h_dict[perm[i]][perm[i + 1]]
        res += h_dict[perm[i + 1]][perm[i]]
    res += h_dict[perm[0]][perm[len(perm) - 1]]
    res += h_dict[perm[len(perm) - 1]][perm[0]]
    return res


filename = 'day13_data.txt'
data = []
with open(filename) as file:
    for line in file:
        data.append(line.strip('.\n'))
names = set()
happy_dict = {}
for line in data:
    name1, name2 = line.split()[0], line.split()[-1]
    names.add(name1)
    names.add(name2)
    if not happy_dict.get(name1):
        happy_dict[name1] = {}
    gl = re.search('(gain|lose) [0-9]*', line).group()
    gl = re.sub('gain ', '', gl)
    gl = int(re.sub('lose ', '-', gl))
    happy_dict[name1][name2] = gl

perms = permutations(names)
print(f"Answer 1: {max([happiness(happy_dict, p) for p in perms])}")

my_name = 'Mr. Lonely'
names.add(my_name)
perms = permutations(names)
for p in happy_dict:
    happy_dict[p][my_name] = 0
happy_dict[my_name] = {name: 0 for name in names}
print(f"Answer 2: {max([happiness(happy_dict, p) for p in perms])}")
