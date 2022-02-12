from itertools import combinations


filename = 'day17_data.txt'
with open(filename) as file:
    data = file.read().split('\n')
liters = 150

ans1 = 0
minn = int(max(data))
for i in range(1, len(data)+1):
    for c in combinations(data, i):
        if sum(map(int, c)) == liters:
            minn = min(minn, i)
            ans1 += 1
print('Answer 1:', ans1)

ans2 = 0
for c in combinations(data, minn):
    if sum(map(int, c)) == liters:
        ans2 += 1
print('Answer 1:', ans2)
