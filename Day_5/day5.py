def handle_arguments(mem, ip, instruction, arg_amount):
    arg_values = []
    x = mem[ip + 1]
    if instruction[-1] == "0":
        x = mem[x]
    arg_values.append(x)

    if arg_amount == 2:
        y = mem[ip + 2]
        if instruction[-2] == "0":
            y = mem[y]
        arg_values.append(y)
    return arg_values

def computer(mem, user_input, ip=0):
    while ip < len(mem):
        op_code = int(str(mem[ip])[-2:])
        instruction = str(mem[ip])[:-2]
        n = 3-len(instruction)
        instruction = instruction.zfill(n + len(instruction))
        args_list = handle_arguments(mem, ip, instruction, 2)

        if op_code == 4:
            arg1, _ = args_list
        else:    # 2,3 arguments
            arg1, arg2 = args_list

        if op_code == 1:
            mem[mem[ip + 3]] = arg1 + arg2
            ip += 4
        elif op_code == 2:
            mem[mem[ip + 3]] = arg1 * arg2
            ip += 4
        elif op_code == 3:
            mem[mem[ip + 1]] = user_input
            ip += 2
        elif op_code == 4:
            print(arg1)
            ip += 2
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
            mem[mem[ip + 3]] = arg1 < arg2
            ip += 4
        elif op_code == 8:
            mem[mem[ip + 3]] = arg1 == arg2
            ip += 4
        else:
            assert op_code == 99
            return

filename = "day5_data.txt"
with open(filename) as file:
    data = list(map(int, file.read().split(',')))
print("Diagnostic code: ", end='')
computer(data, 5)