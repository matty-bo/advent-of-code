import math as m
from collections import defaultdict

def parse(s):
    c, i = s.split(' ')
    return int(c), i

def ore_cost(count, product):
    need = defaultdict(int, {product: count})
    have = defaultdict(int)
    ore = 0
    while need:
        item = list(need.keys())[0]
        if have[item] >= need[item]:
            have[item] -= need[item]
            del need[item]
            continue
        needed_count = need[item] - have[item]
        del need[item]
        del have[item]
        produced_count = qt_prod[item]
        reactions_count = m.ceil(needed_count / produced_count)
        have[item] += reactions_count * produced_count - needed_count
        for count, name in reactions[item]:
            if name == 'ORE':
                ore += count * reactions_count
            else:
                need[name] += count * reactions_count
    return ore


def bs(x, l, u):
    if u < l:
        return -1
    fuel_qt = l + (u - l) // 2
    cost = ore_cost(fuel_qt, 'FUEL')
    fuels.append((fuel_qt, cost))
    if cost == x:
        return fuel_qt
    if cost > x:
        return bs(x, l, fuel_qt - 1)
    else:
        return bs(x, fuel_qt + 1, u)


filename = 'day14_data.txt'
reactions = {}
qt_prod = {}
with open(filename) as file:
    for line in file.readlines():
        line = line.strip()
        substracts, product = line.split(' => ')
        substracts = substracts.split(', ')
        substracts = [parse(s) for s in substracts]
        nprod, prod = parse(product)
        qt_prod[prod] = nprod
        reactions[prod] = substracts


ans1 = ore_cost(1, 'FUEL')
print('Task 1:', ans1)

fuels = []
trillion = 1e12
lb = trillion // ans1
ub = lb * 2
bs(trillion, lb, ub)
ans2 = int([f for f, c in fuels if c < trillion][-1:][0])
print('Task 2:', ans2)