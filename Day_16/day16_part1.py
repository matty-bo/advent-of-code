import collections

def pattern(pos, input):
    b = collections.deque([0, 1, 0, -1])
    p = collections.deque([])
    while len(p) <= len(input):
        if not b:
            b = collections.deque([0, 1, 0, -1])
        temp = b[0]
        b.popleft()
        for _ in range(pos):
            p.append(temp)
            if len(p) == len(input)+1:
                p.popleft()
                return p
    p.popleft()
    return p

def phase(input):
    output = []
    for i in range(len(input)-1, len(input)//2, -1):
        number = 0
        if output:
            number = int(output[-1]) + int(input[i])
        else:
            number = int(input[i])
        output.append(number % 10)
    for i in range(len(input)//2, -1, -1):
        number = 0
        p = pattern(i + 1, input)
        for j in range(len(input) - 1, i - 1, -1):
            number += int(input[j]) * p[j]
        output.append(abs(number) % 10)
    return output

filename = "day16_data.txt"
with open(filename) as file:
    data = file.read()
output = data
for _ in range(100):
    output = phase(output)[::-1]
ans1 = ''.join(map(str, output[:8]))
print(ans1)
