import re


with open('input10') as file:
    data = file.read()
sv = re.findall('value (.+) goes to bot (.+)', data)
bots = {}
for v, b in sv:
    if int(b) not in bots:
        bots[int(b)] = [int(v)]
    else:
        bots[int(b)].append(int(v))

data = re.sub('value .+ goes to bot .+\n*', '', data).split('\n')
data = [line for line in data if line]
actions = []
for line in data:
    x = re.search('bot (.+) gives low to (.+ .+) and high to (.+)', line)
    actions.append([x.group(i).split() for i in range(1, 4)])
for a in actions:
    a[0][0] = int(a[0][0])
    a[1][1] = int(a[1][1])
    a[2][1] = int(a[2][1])

ans1 = 0
outputs = {}
while actions:
    for a in actions:
        giver_nr = a[0][0]
        takers = [(a[1][0], a[1][1]), (a[2][0], a[2][1])]
        taker_l, nr_l = a[1][0], a[1][1]
        taker_h, nr_h = a[2][0], a[2][1]
        if giver_nr in bots and len(bots.get(giver_nr)) == 2:
            low_high = min(bots[giver_nr]), max(bots[giver_nr])
            if low_high == (17, 61):
                ans1 = giver_nr
            for i in range(2):
                if takers[i][0] == 'bot':
                    if takers[i][1] not in bots:
                        bots[takers[i][1]] = [low_high[i]]
                    else:
                        bots[takers[i][1]].append(low_high[i])
                elif takers[i][0] == 'output':
                    if takers[i][1] not in outputs:
                        outputs[takers[i][1]] = [low_high[i]]
                    else:
                        outputs[takers[i][1]].append(low_high[i])
            bots[giver_nr].remove(low_high[0])
            bots[giver_nr].remove(low_high[1])
            actions.remove(a)
print('Answer 1:', ans1)
print('Answer 2:', outputs[0][0]*outputs[1][0]*outputs[2][0])
