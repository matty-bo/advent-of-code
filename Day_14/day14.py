import re
from itertools import product


def bin36(nr):
    binary = [bit for bit in bin(nr)[2:]]
    return ['0' for i in range(36 - len(binary))] + binary


def apply_mask(nr, mask):
    for i in range(len(mask)):
        if mask[i] != 'X':
            nr[i] = mask[i]
    return ''.join(nr)


def apply_mask2(nr, mask):
    for i in range(len(mask)):
        if mask[i] == '1':
            nr[i] = '1'
        elif mask[i] == 'X':
            nr[i] = 'X'
    return ''.join(nr)


def get_possible_addresses(nr):
    count_x = nr.count('X')
    perms = list(map(list, product('01', repeat=count_x)))
    addresses = []
    for p in perms:
        a = []
        for bit in nr:
            if bit != 'X':
                a.append(bit)
            else:
                a.append(p.pop())
        int_address = int(''.join(a), 2)
        addresses.append(int_address)
    return addresses


filename = 'input14.txt'
with open(filename) as file:
    data = file.readlines()

part1_memory = {}
part2_memory = {}
for line in data:
    mask_match = re.match(r'mask = (.+)\n', line)
    mem_match = re.match(r'mem\[(.+)\] = (.+)', line)
    if mask_match:
        mask = mask_match.group(1)
    elif mem_match:
        # part 1
        ea, val = int(mem_match.group(1)), int(mem_match.group(2))
        part1_memory[ea] = int(apply_mask(bin36(val), mask), 2)
        # part 2
        eax = apply_mask2(bin36(ea), mask)
        addresses = get_possible_addresses(eax)
        for a in addresses:
            part2_memory[a] = val
ans1 = sum(part1_memory.values())
ans2 = sum(part2_memory.values())
print('Answer 1:', ans1)
print('Answer 2:', ans2)
