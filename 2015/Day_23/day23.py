import re


def computer(data):
    address = 0
    while 0 <= address < len(data):
        if data[address][0] == 'hlf':
            registers[data[address][1]] /= 2
            address += 1
        elif data[address][0] == 'tpl':
            registers[data[address][1]] *= 3
            address += 1
        elif data[address][0] == 'inc':
            registers[data[address][1]] += 1
            address += 1
        elif data[address][0] == 'jmp':
            address += int(data[address][1])
        elif data[address][0] == 'jie':
            if registers[data[address][1]] % 2 == 0:
                address += int(data[address][2])
            else:
                address += 1
        elif data[address][0] == 'jio':
            if registers[data[address][1]] == 1:
                address += int(data[address][2])
            else:
                address += 1


filename = 'day23_data.txt'
data = []
with open(filename) as file:
    for line in file:
        data.append(re.sub('[,+\n]', '', line).split())
registers = {'a': 0, 'b': 0}
computer(data)
print('Answer 1:', registers['b'])
registers = {'a': 1, 'b': 0}
computer(data)
print('Answer 2:', registers['b'])