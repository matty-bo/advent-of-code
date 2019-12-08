def answer():
    filename = "day2_data.txt"
    clean_data = load_data(filename)
    data = clean_data.copy()
    intcode_computer(data)
    print("Task 1:", data[0])
    print("Task 2:", find_pairs(clean_data))


def intcode_computer(numbers):
    for i in range(0, len(numbers), 4):
        op_code = numbers[i]
        if op_code == 1:
            numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
        elif op_code == 2:
            numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
        elif op_code == 99:
            return
        else:
            # print("Wrong operation code!")
            return
    return numbers


def load_data(filename):
    with open(filename) as file:
        data = file.read()
        data = data.split(sep=',')
        data = list(map(int, data))
    return data


def calculate_output(data, noun, verb):
    data[1] = noun
    data[2] = verb
    intcode_computer(data)
    return data[0]


def find_pairs(clear_data):

    for noun in range(0, 100):
        for verb in range(0, 100):
            data = clear_data.copy()
            if calculate_output(data, noun, verb) == 19690720:
                return 100*noun+verb


answer()
