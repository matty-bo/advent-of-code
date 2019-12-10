import itertools


def load_data(filename):
    with open(filename) as file:
        data = file.read()
        data = data.split(sep=',')
        data = list(map(int, data))
    return data


def handle_arguments(data, i, instruction, arg_amount):
    arg_values = []

    if arg_amount == 1 or 2:
        x = data[i + 1]
        if instruction[-1] == "0":
            x = data[x]
        arg_values.append(x)

    if arg_amount == 2:
        y = data[i + 2]
        if instruction[-2] == "0":
            y = data[y]
        arg_values.append(y)

    return arg_values


def amplifier(data, inputs, ip):
    while ip < len(data):
        op_code = int(str(data[ip])[-2:])
        instruction = str(data[ip])[:-2]
        n = 3 - len(instruction)
        arg1, arg2 = -1, -1
        instruction = instruction.zfill(n + len(instruction))

        # setting arguments for instructions according to parametres
        # 1 argument
        if op_code in [3, 4]:
            args_list = handle_arguments(data, ip, instruction, 1)
            arg1 = args_list[0]

        # 2 arguments
        if op_code in [5, 6]:
            args_list = handle_arguments(data, ip, instruction, 2)
            arg1, arg2 = args_list

        # 3 arguments
        elif op_code in [1, 2, 7, 8]:
            args_list = handle_arguments(data, ip, instruction, 2)
            arg1, arg2 = args_list

        # OP CODES HANDLING
        if op_code == 1:
            data[data[ip + 3]] = arg1 + arg2
            ip += 4

        elif op_code == 2:
            data[data[ip + 3]] = arg1 * arg2
            ip += 4

        # INPUTS
        elif op_code == 3:
            arg1 = data[ip+1]
            data[arg1] = inputs[0]
            inputs.pop(0)
            ip += 2

        # OUTPUTS
        elif op_code == 4:
            output = arg1
            ip += 2
            return output, ip

        elif op_code == 5:
            if arg1 != 0:
                ip = arg2
            else:
                ip += 3

        elif op_code == 6:
            if arg1 == 0:
                ip = arg2
            else:
                ip += 3

        elif op_code == 7:
            if arg1 < arg2:
                data[data[ip + 3]] = 1
            else:
                data[data[ip + 3]] = 0
            ip += 4

        elif op_code == 8:
            if arg1 == arg2:
                data[data[ip + 3]] = 1
            else:
                data[data[ip + 3]] = 0
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
            out, _ = amplifier(data, inputs, 0)  # amplifier A
        if out > max_thruster:
            max_thruster = out
    return max_thruster


def loop_max_thruster(data):
    perms = list(itertools.permutations(range(5, 10)))

    max_thruster = 0
    for perm in perms:
        output = 0
        ips = [0 for _ in range(5)]
        outs = [0 for _ in range(5)]
        inputs = [[perm[i]] for i in range(5)]
        inputs[0].append(0)

        halted = False
        while not halted:
            for i in range(5):
                output, next_ip = amplifier(data, inputs[i], ips[i])
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


def answer():
    filename = "day7_data.txt"
    data = load_data(filename)
    print("Task 1:", find_max_thruster(data))
    print("Task 2:", loop_max_thruster(data))


answer()
