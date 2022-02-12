filename = 'input9.txt'
with open(filename) as file:
    data = [int(nr) for nr in file.readlines()]
pre_len = 25

nr = None
i = 0
sums = True
while sums:
    prev, nr = data[i: i + pre_len], data[i + pre_len]
    diffs = {p: nr - p for p in prev}
    is_sum = [diffs[key] in diffs for key in diffs if diffs[key] != key]
    sums = any(is_sum)
    i += 1
print('Answer 1:', nr)

i, j, s = 0, 0, 0
while s != nr:
    j = i
    s = 0
    while s < nr:
        s += data[j]
        j += 1
    i += 1
ans2 = min(data[i: j]) + max(data[i: j])
print('Answer 2:', ans2)
