import itertools

def ga(mem, modes, ip, shift):
    if modes[-shift] == "0":
        return mem[ip + shift]
    return ip + shift

def computer(memory, inputs, ip):
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)

        if op_code == 1:
            memory[memory[ip + 3]] = memory[ga(memory, modes, ip, 1)] + memory[ga(memory, modes, ip, 2)]
            ip += 4
        elif op_code == 2:
            memory[memory[ip + 3]] = memory[ga(memory, modes, ip, 1)] * memory[ga(memory, modes, ip, 2)]
            ip += 4
        elif op_code == 3:  # INPUTS
            memory[memory[ip + 1]] = inputs[0]
            inputs.pop(0)
            ip += 2
        elif op_code == 4:  # OUTPUTS
            output = memory[ga(memory,modes,ip,1)]
            ip += 2
            return output, ip
        elif op_code == 5:
            if memory[ga(memory, modes, ip, 1)] != 0:
                ip = memory[ga(memory, modes, ip, 2)]
            else:
                ip += 3
        elif op_code == 6:
            if memory[ga(memory, modes, ip, 1)] == 0:
                ip = memory[ga(memory, modes, ip, 2)]
            else:
                ip += 3
        elif op_code == 7:
            memory[memory[ip + 3]] = memory[ga(memory, modes, ip, 1)] < memory[ga(memory, modes, ip, 2)]
            ip += 4
        elif op_code == 8:
            memory[memory[ip + 3]] = memory[ga(memory, modes, ip, 1)] == memory[ga(memory, modes, ip, 2)]
            ip += 4
        else:
            assert op_code == 99
            return None, ip

def find_max_thruster(data):
    perms = list(itertools.permutations(range(0, 5)))
    max_thruster = 0
    for perm in perms:
        out = 0
        for i in range(5):
            inputs = [perm[i], out]
            out, _ = computer(data, inputs, 0)  # amplifier A
        if out > max_thruster:
            max_thruster = out
    return max_thruster

def loop_max_thruster(data):
    perms = list(itertools.permutations(range(5, 10)))
    max_thruster = 0
    for perm in perms:
        ips = [0 for _ in range(5)]
        outs = [0 for _ in range(5)]
        inputs = [[perm[i]] for i in range(5)]
        inputs[0].append(0)
        halted = False
        while not halted:
            for i in range(5):
                output, next_ip = computer(data, inputs[i], ips[i])
                if output is None:
                    if outs[-1] > max_thruster:
                        max_thruster = outs[-1]
                    halted = True
                    break
                ips[i] = next_ip
                if output is not None:
                    outs[i] = output
                inputs[(i + 1) % len(inputs)].append(output)
    return max_thruster

filename = "day7_data.txt"
with open(filename) as file:
    data = list(map(int, file.read().split(',')))
print("Task 1:", find_max_thruster(data))
print("Task 2:", loop_max_thruster(data))