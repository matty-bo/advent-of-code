def handle_arguments(numbers, i, instruction, arg_amount):
    arg_values = []

    if arg_amount == 1 or 2:
        x = numbers[i+1]
        if instruction[-1] == "0":
            x = numbers[x]
        arg_values.append(x)

    if arg_amount == 2:
        y = numbers[i+2]
        if instruction[-2] == "0":
            y = numbers[y]
        arg_values.append(y)

    return arg_values


def intcode_computer(numbers, user_input):
    i = 0
    while i < len(numbers):
        op_code = int(str(numbers[i])[-2:])
        instruction = str(numbers[i])[:-2]
        n = 3-len(instruction)
        arg1, arg2 = -1, -1
        instruction = instruction.zfill(n + len(instruction))

        # setting arguments for instructions according to parametres
        # 1 argument
        if op_code in [3, 4]:
            args_list = handle_arguments(numbers, i, instruction, 1)
            arg1 = args_list[0]

        # 2 arguments
        if op_code in [5, 6]:
            args_list = handle_arguments(numbers, i, instruction, 2)
            arg1, arg2 = args_list
        # 3 arguments

        elif op_code in [1, 2, 7, 8]:
            args_list = handle_arguments(numbers, i, instruction, 2)
            arg1, arg2 = args_list

        # OP CODES HANDLING
        if op_code == 1:
            numbers[numbers[i + 3]] = arg1 + arg2
            i += 4

        elif op_code == 2:
            numbers[numbers[i + 3]] = arg1 * arg2
            i += 4

        elif op_code == 3:
            numbers[numbers[i+1]] = user_input
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
            if arg1 < arg2:
                numbers[numbers[i+3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i += 4

        elif op_code == 8:
            if arg1 == arg2:
                numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i += 4

        elif op_code == 99:
            return numbers
        else:
            i += 1

    return numbers


def load_data(filename):
    with open(filename) as file:
        data = file.read()
        data = data.split(sep=',')
        data = list(map(int, data))
    return data


def answer():
    filename = "day5_data.txt"
    data = load_data(filename)
    number = int(input("Wprowadź ID: "))
    print ("Diagnostic code: ", end='')
    intcode_computer(data, number)


answer()
