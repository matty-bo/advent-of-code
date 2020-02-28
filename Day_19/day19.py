import re


def replace(string, replacements):
    molecules = set()
    for s, p in replacements:
        for i in range(len(string)):
            if string[i:i+len(s)] == s:
                x = string[:i] + p + string[i+len(s):]
                molecules.add(x)
    return len(molecules)

filename = 'day19_data.txt'
with open(filename) as file:
    data = [line.strip() for line in file]
medicine, data = data[-1], data[:-2]
data = [re.findall('(\w+) => (\w+)', line)[0] for line in data]
print('Answer 1:', replace(medicine, data))

ans2 = 0
result = medicine
while result != 'e':
    med = result
    for s, p in data:
        if p in result:
            result = result.replace(p, s, 1)
            ans2 += 1
print('Answer 2:', ans2)
