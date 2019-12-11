def computer(mem):
    for i in range(0, len(mem), 4):
        op_code = mem[i]
        if op_code == 1:
            mem[mem[i + 3]] = mem[mem[i + 1]] + mem[mem[i + 2]]
        elif op_code == 2:
            mem[mem[i + 3]] = mem[mem[i + 1]] * mem[mem[i + 2]]
        elif op_code == 99:
            return mem[0]

def calculate_output(data, noun, verb):
    data[1], data[2] = noun, verb
    return computer(data)

def find_inputs(mem):
    for noun in range(0, 100):
        for verb in range(0, 100):
            if calculate_output(mem.copy(), noun, verb) == 19690720:
                return 100*noun+verb

def load_data(filename):
    with open(filename) as file:
        data = file.read().split(',')
        data = list(map(int, data))
    return data

filename = "day2_data.txt"
print("Task 1:", computer(load_data(filename)))
print("Task 2:", find_inputs(load_data(filename)))