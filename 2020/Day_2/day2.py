import re


filename = 'input2.txt'
with open(filename) as file:
    data = list(map(lambda x: x.rstrip().replace(': ', ':'), file.readlines()))

data = list(map(lambda x: re.split(r'[-:\s]', x), data))
data = list(map(lambda x: (int(x[0]), int(x[1]), x[2], x[3]), data))

ans1 = sum(p[0] <= p[3].count(p[2]) <= p[1] for p in data)
print('Answer 1:', ans1)

ans2 = sum((p[3][p[0] - 1] == p[2]) != (p[3][p[1] - 1] == p[2]) for p in data)
print('Answer 2:', ans2)
