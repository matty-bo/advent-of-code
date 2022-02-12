class Computer:
    def __init__(self):
        self.accumulator = 0
        self.executed = set()
        self.halted = 0
        self.ip = 0
        self.instruction_set = {'acc': self.acc,
                                'jmp': self.jmp,
                                'nop': self.nop}

    def acc(self, *args):
        self.accumulator += args[0]
        self.ip += 1

    def jmp(self, *args):
        self.ip += args[0]

    def nop(self, *args):
        self.ip += 1

    def compile(self, data):
        while self.ip not in self.executed and self.ip < len(data):
            ins, val = data[self.ip]
            self.executed.add(self.ip)
            self.instruction_set[ins](val)
        self.halted = self.ip >= len(data)
        return self.accumulator

    def reset(self):
        self.accumulator = 0
        self.executed = set()
        self.halted = 0
        self.ip = 0


filename = 'input8.txt'
with open(filename) as file:
    data = list(map(lambda x: (x.split()[0], int(x.split()[1])), file.readlines()))
computer = Computer()
ans1 = computer.compile(data)
print('Answer 1:', ans1)

ans2 = -1
rev = {'nop': 'jmp', 'jmp': 'nop'}
swap_indexes = [data.index(x) for x in data if x[0] in rev]
for idx in swap_indexes:
    computer.reset()
    data[idx] = rev[data[idx][0]], data[idx][1]
    ans2 = computer.compile(data)
    data[idx] = rev[data[idx][0]], data[idx][1]
    if computer.halted:
        break

print('Answer 2:', ans2)
