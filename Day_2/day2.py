filename = 'day2_data.txt'
data = []
with open(filename) as file:
    for line in file.readlines():
        data.append(list(map(int, line.strip('\n').split(sep='x'))))

ans1 = 0
ans2 = 0
for p in data:
    paper = 2*p[0]*p[1] + 2*p[1]*p[2] + 2*p[2]*p[0]
    ribbon = p[0] * p[1] * p[2]
    p.remove(max(p))
    ans1 += paper + p[0] * p[1]
    ans2 += ribbon + 2*p[0] + 2*p[1]
print('Answer 1:', ans1)
print('Answer 2:', ans2)
