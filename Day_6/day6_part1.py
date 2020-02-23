def orbit_checksum(name):
    count = 0
    for child in data.get(name, []):
        count += 1
        count += orbit_checksum(child)
    return count


filename = "day6_data.txt"
data = {}
with open(filename) as file:
    for line in file.readlines():
        p, c = line.strip().split(')')
        if p not in data:
            data[p] = []
        data[p].append(c)
ans1 = 0
for line in data:
    ans1 += orbit_checksum(line)
print('Answer 1:', ans1)

