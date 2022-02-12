import re

tape = {'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1}

aunts = {}
filename = 'day16_data.txt'
with open(filename) as file:
    for line in file:
        line = re.sub('^Sue |:|,', '', line.strip()).split()
        aunts[line[0]] = {line[1]: int(line[2]),
                          line[3]: int(line[4]),
                          line[5]: int(line[6])}
suspects = []
for a in aunts:
    for info in tape:
        try:
            if aunts[a][info] == tape[info]:
                suspects.append(a)
        except:
            pass
ans1 = [s for s in suspects if suspects.count(s) == 3][0]
print('Answer 1:', ans1)

suspects.clear()
for a in aunts:
    for info in tape:
        try:
            cond = False
            if info in ['cats', 'trees'] and aunts[a][info] > tape[info]:
                cond = True
            elif info in ['pomeranians', 'goldfish'] and aunts[a][info] < tape[info]:
                cond = True
            elif aunts[a][info] == tape[info]:
                cond = True
            if cond:
                suspects.append(a)
        except:
            pass
ans2 = [s for s in suspects if suspects.count(s) == 3][0]
print('Answer 2:', ans2)
