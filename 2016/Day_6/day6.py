with open('input6.txt') as file:
    data = [line.strip() for line in file]
ans1, ans2 = [], []
for i in range(len(data[0])):
    occ = {row[i]: 0 for row in data}
    for char in (row[i] for row in data):
        occ[char] += 1
    ans1.append(max(occ, key=occ.get))
    ans2.append(min(occ, key=occ.get))
print('Answer 1:', ''.join(ans1))
print('Answer 2:', ''.join(ans2))
