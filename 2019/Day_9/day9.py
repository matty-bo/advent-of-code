def ga(modes, ip, shift, rel_base):
    if modes[-shift] == "0":
        return memory[ip + shift]
    elif modes[-shift] == "1":
        return ip + shift
    elif modes[-shift] == "2":
        return memory[ip + shift] + rel_base

def computer(memory, user_input, ip=0):
    rel_base = 0
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] + memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 2:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] * memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 3:
            memory[ga(modes, ip, 1, rel_base)] = user_input
        elif op_code == 4:
            print(memory[ga(modes, ip, 1, rel_base)])
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

filename = "day9_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
for i in range(len(memory) * 10):
    memory.append(0)
print("Task 1: ", end="")
computer(memory, 1)
print("Task 2: ", end="")
computer(memory, 2)