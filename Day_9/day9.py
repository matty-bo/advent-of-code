def handle_arguments(numbers, i, instruction, arg_amount, rel_base):
    arg_values = []

    if arg_amount == 1 or 2:
        x = numbers[i+1]
        if instruction[-1] == "0":
            x = numbers[x]
        elif instruction[-1] == "2":
            x = numbers[x+rel_base]
        arg_values.append(x)

    if arg_amount == 2:
        y = numbers[i+2]
        if instruction[-2] == "0":
            y = numbers[y]
        elif instruction[-2] == "2":
            y = numbers[y + rel_base]
        arg_values.append(y)

    return arg_values


def intcode_computer(numbers, user_input):
    i = 0
    rel_base = 0
    while i < len(numbers):
        op_code = int(str(numbers[i])[-2:])
        instruction = str(numbers[i])[:-2]
        n = 3-len(instruction)
        arg1, arg2 = 0, 0
        instruction = instruction.zfill(n + len(instruction))

        # setting arguments for instructions according to parametres
        # 1 argument
        if op_code in [3, 4, 9]:
            args_list = handle_arguments(numbers, i, instruction, 1, rel_base)
            arg1 = args_list[0]

        # 2 arguments
        if op_code in [5, 6]:
            args_list = handle_arguments(numbers, i, instruction, 2, rel_base)
            arg1, arg2 = args_list

        # 3 arguments
        elif op_code in [1, 2, 7, 8]:
            args_list = handle_arguments(numbers, i, instruction, 2, rel_base)
            arg1, arg2 = args_list

        #parameter for saving to is in relative mode
        wr_arg_relative = 0


        # OP CODES HANDLING
        if op_code == 1:
            if instruction[-3] == "2":
                wr_arg_relative = rel_base
            numbers[numbers[i + 3]+wr_arg_relative] = arg1 + arg2
            i += 4

        elif op_code == 2:
            if instruction[-3] == "2":
                wr_arg_relative = rel_base
            numbers[numbers[i + 3]+wr_arg_relative] = arg1 * arg2
            i += 4

        elif op_code == 3:
            if instruction[-1] == "2":
                wr_arg_relative = rel_base
            numbers[numbers[i+1]+wr_arg_relative] = user_input
            i += 2

        elif op_code == 4:
            print(arg1)
            i += 2

        elif op_code == 5:
            if arg1 != 0:
                i = arg2
            else:
                i += 3

        elif op_code == 6:
            if arg1 == 0:
                i = arg2
            else:
                i += 3

        elif op_code == 7:
            if instruction[-3] == "2":
                wr_arg_relative = rel_base
            if arg1 < arg2:
                numbers[numbers[i+3]+wr_arg_relative] = 1
            else:
                numbers[numbers[i + 3]+wr_arg_relative] = 0
            i += 4

        elif op_code == 8:
            if instruction[-3] == "2":
                wr_arg_relative = rel_base
            if arg1 == arg2:
                numbers[numbers[i + 3]+wr_arg_relative] = 1
            else:
                numbers[numbers[i + 3]+wr_arg_relative] = 0
            i += 4

        elif op_code == 9:
            rel_base += arg1
            i += 2

        elif op_code == 99:
            return numbers
    return -1


def load_data(filename):
    with open(filename) as file:
        data = file.read()
        data = data.split(sep=',')
        data = list(map(int, data))
    return data


def answer():
    filename = "day9_data.txt"
    data = load_data(filename)
    for i in range(len(data) * 10):
        data.append(0)

    number = 1
    print("Task 1: ", end="")
    intcode_computer(data, number)

    number = 2
    print("Task 2: ", end="")
    intcode_computer(data, number)

answer()
