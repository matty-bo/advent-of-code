filename = 'input6.txt'
with open(filename) as file:
    data = file.read().split('\n\n')

ans1 = sum(len({char for char in s if char != '\n'}) for s in data)
print('Answer 1:', ans1)

group_sets = [[{char for char in answers} for answers in g.split()] for g in data]
everyone = [len(g[0].intersection(*g[1:])) for g in group_sets]
ans2 = sum(everyone)
print('Answer 2:', ans2)
