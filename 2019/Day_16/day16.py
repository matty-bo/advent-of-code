from collections import deque


def pattern(pos, input):
    b = deque([0, 1, 0, -1])
    p = deque([])
    while len(p) <= len(input):
        if not b:
            b = deque([0, 1, 0, -1])
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


def phase2(inp):
    cum_sum = sum(inp)
    sig_out = []
    for i in range(len(inp)):
        sig_out.append(cum_sum % 10)
        cum_sum -= inp[i]
    return sig_out


filename = "day16_data.txt"
with open(filename) as file:
    inp = file.read()
offset = int(inp[:7])

sig1 = inp
for _ in range(100):
    sig1 = phase(sig1)[::-1]
ans1 = ''.join(map(str, sig1[:8]))
print('Answer 1:', ans1)

inp *= 10000
inp = list(map(int, inp))
sig2 = inp[offset: ]

for i in range(100):
    sig2 = phase2(sig2)

print('Answer 2:', ''.join(list(map(str, sig2[:8]))))
