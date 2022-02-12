def compute(name):
    try:
        return int(name)
    except:
        pass
    if name not in results:
        inst = instructions[name]
        if len(inst) == 1:
            signal = compute(inst[0])
        else:
            op = inst[-2]
            if op == 'NOT':
                signal = ~compute(inst[1]) & 0xffff
            elif op == 'AND':
                signal = compute(inst[0]) & compute(inst[2])
            elif op == 'OR':
                signal = compute(inst[0]) | compute(inst[2])
            elif op == 'LSHIFT':
                signal = compute(inst[0]) << compute(inst[2])
            elif op == 'RSHIFT':
                signal = compute(inst[0]) >> compute(inst[2])
        results[name] = signal
    return results[name]


filename = 'day7_data.txt'
with open(filename) as file:
    data = file.readlines()
instructions = {}
results = {}
for row in data:
    ops, res = row.split('->')
    instructions[res.strip()] = ops.strip().split(' ')
ans1 = compute('a')
instructions['b'] = [ans1]
results.clear()
ans2 = compute('a')
print('Answer 1:', ans1)
print('Answer 2:', ans2)
