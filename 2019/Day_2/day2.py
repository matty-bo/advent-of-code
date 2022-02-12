def computer(mem):
    for i in range(0, len(mem), 4):
        op_code = mem[i]
        if op_code == 1:
            mem[mem[i + 3]] = mem[mem[i + 1]] + mem[mem[i + 2]]
        elif op_code == 2:
            mem[mem[i + 3]] = mem[mem[i + 1]] * mem[mem[i + 2]]
        elif op_code == 99:
            return mem[0]

def find_inputs(mem):
    for noun in range(0, 100):
        for verb in range(0, 100):
            data = mem.copy()
            data[1], data[2] = noun,  verb
            if computer(data) == 19690720:
                return 100*noun+verb

filename = "day2_data.txt"
with open(filename) as file:
    data = list(map(int, file.read().split(',')))
print("Task 1:", computer(data.copy()))
print("Task 2:", find_inputs(data))