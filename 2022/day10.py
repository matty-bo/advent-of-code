class CPU:
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.signal_sum = 0

    def execute(self, instruction):
        if instruction.startswith('addx'):
            for _ in range(2):
                self.cycle += 1
                yield self.cycle, self.X

            _, value = instruction.split(' ')
            value = int(value)
            self.X += value

        elif instruction == 'noop':
            self.cycle += 1
            yield self.cycle, self.X


class CRT:
    def __init__(self, rows=6, cols=40):
        self.rows = rows
        self.cols = cols
        self.screen = ['' for _ in range(cols * rows)]

    def get_screen(self):
        formatted_output = ""
        for i in range(0, len(self.screen), self.cols):
            row = self.screen[i: i + self.cols]
            formatted_output += ''.join(row) + '\n'
        return formatted_output

    def draw_pixel(self, pixel, position):
        self.screen[position] = pixel


def main():
    filename = "inputs/input10"
    with open(filename) as file:
        instructions = [line for line in file.read().splitlines()]
    ans1 = part1(instructions)
    ans2 = part2(instructions)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2:\n{ans2}')


def part1(instructions):
    cpu = CPU()
    ans = 0
    for instruction in instructions:
        for cycle, X in cpu.execute(instruction):
            if (cycle + 20) % 40 == 0:
                ans += cycle * X
    return ans


def part2(instructions):
    cpu = CPU()
    crt = CRT()
    for instruction in instructions:
        for cycle, X in cpu.execute(instruction):
            sprite_position = (X - 1, X, X + 1)
            pixel_position = cycle - 1
            if pixel_position % crt.cols in sprite_position:
                pixel = '#'
            else:
                pixel = '.'
            crt.draw_pixel(pixel, pixel_position)
    ans = crt.get_screen()
    return ans


if __name__ == '__main__':
    main()
