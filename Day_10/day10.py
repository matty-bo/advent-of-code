filename = 'input10.txt'
with open(filename) as file:
    data = [int(nr) for nr in file.readlines()]
data += [0, max(data) + 3]
data = sorted(data)

diffs = {1: 0, 2: 0, 3: 0}
for i in range(len(data) - 1):
    diff = data[i+1] - data[i]
    diffs[diff] += 1
ans1 = diffs[1] * diffs[3]
print('Answer 1:', ans1)

i = 1
ans2 = 1
count = 0
len_mult = {1: 2, 2: 4, 3: 7}
while i < len(data) - 1:
    diff = data[i+1] - data[i]
    diff2 = data[i] - data[i - 1]
    if diff < 3 and diff2 < 3:
        count += 1
    else:
        if count:
            ans2 *= len_mult[count]
        count = 0
    i += 1
print('Answer 2:', ans2)
