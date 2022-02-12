class Computer:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.ip = 0
        self.registers = {'a': a, 'b': b, 'c': c, 'd': d}

    def reset(self):
        self.__init__()

    def execute(self, program):
        while self.ip < len(program):
            instruction = program[self.ip]
            if instruction[0] == 'cpy':
                self.cpy(instruction[1], instruction[2])
            elif instruction[0] == 'inc':
                self.inc(instruction[1])
            elif instruction[0] == 'dec':
                self.dec(instruction[1])
            elif instruction[0] == 'jnz':
                self.jnz(instruction[1], instruction[2])
        return self.registers

    def cpy(self, x, y):
        x = int(self.registers.get(x, x))
        self.registers[y] = x
        self.ip += 1

    def inc(self, x):
        self.registers[x] += 1
        self.ip += 1

    def dec(self, x):
        self.registers[x] -= 1
        self.ip += 1

    def jnz(self, x, y):
        if int(self.registers.get(x, x)) != 0:
            self.ip += int(y)
        else:
            self.ip += 1


with open('input12.txt') as file:
    program = [line.strip().split() for line in file]
print('Answer 1:', Computer().execute(program)['a'])
print('Answer 2:', Computer(c=1).execute(program)['a'])
