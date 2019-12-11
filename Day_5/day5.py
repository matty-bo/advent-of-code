def ga(modes, ip, shift):
    if modes[-shift] == "0":
        return memory[ip + shift]
    return ip + shift

def computer(memory, user_input, ip=0):
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[memory[ip + 3]] = memory[ga(modes, ip, 1)] + memory[ga(modes, ip, 2)]
        elif op_code == 2:
            memory[memory[ip + 3]] = memory[ga(modes, ip, 1)] * memory[ga(modes, ip, 2)]
        elif op_code == 3:
            memory[memory[ip + 1]] = user_input
        elif op_code == 4:
            print(memory[ga(modes, ip, 1)])
        elif op_code == 5:
            if memory[ga(modes, ip, 1)] != 0:
                ip = memory[ga(modes, ip, 2)]
            else:
                ip += 3
        elif op_code == 6:
            if memory[ga(modes, ip, 1)] == 0:
                ip = memory[ga(modes, ip, 2)]
            else:
                ip += 3
        elif op_code == 7:
            memory[memory[ip + 3]] = memory[ga(modes, ip, 1)] < memory[ga(modes, ip, 2)]
        elif op_code == 8:
            memory[memory[ip + 3]] = memory[ga(modes, ip, 1)] == memory[ga(modes, ip, 2)]
        else:
            assert op_code == 99
            return
        if op_code in [1, 2, 7, 8]:
            ip += 4
        elif op_code in [3, 4]:
            ip += 2

filename = "day5_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
computer(memory, 5)