def ga(modes, ip, shift, rel_base):
    if modes[-shift] == "0":
        return memory[ip + shift]
    elif modes[-shift] == "1":
        return ip + shift
    elif modes[-shift] == "2":
        return memory[ip + shift] + rel_base


def computer(memory, user_input, ip=0):
    rel_base = 0
    read_x = True

    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] + memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 2:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] * memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 3:
            if read_x:
                cord = user_input[0]
            else:
                cord = user_input[1]
            read_x = not read_x
            memory[ga(modes, ip, 1, rel_base)] = cord
        elif op_code == 4:
            out = memory[ga(modes, ip, 1, rel_base)]
            return out
        elif op_code == 5:
            if memory[ga(modes, ip, 1, rel_base)] != 0:
                ip = memory[ga(modes, ip, 2, rel_base)]
            else:
                ip += 3
        elif op_code == 6:
            if memory[ga(modes, ip, 1, rel_base)] == 0:
                ip = memory[ga(modes, ip, 2, rel_base)]
            else:
                ip += 3
        elif op_code == 7:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] < memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 8:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] == memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 9:
            rel_base += memory[ga(modes, ip, 1, rel_base)]
        else:
            assert op_code == 99
            return
        if op_code in [1, 2, 7, 8]:
            ip += 4
        elif op_code in [3, 4, 9]:
            ip += 2


def find_cords():
    rows, cols = 2000, 2000
    for y in range(1000, rows):
        for x in range(y//2, cols):
            is_pulled = computer(memory.copy(), (x, y))
            if is_pulled:
                corner = computer(memory.copy(), (x + 99, y - 99))
                if corner:
                    return x, y - 99
                else:
                    break
    return 0, 0


filename = "day19_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
memory += [0 for i in range(len(memory) * 10)]

ans1 = sum([computer(memory.copy(), (x, y)) for y in range(50) for x in range(50)])

x, y = find_cords()
ans2 = x * 10000 + y

print(f'Answer 1: {ans1}')
print(f'Answer 2: {ans2}')
