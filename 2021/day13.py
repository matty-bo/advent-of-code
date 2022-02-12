import numpy as np


def main():
    filename = "inputs/input13"
    with open(filename) as file:
        points, instructions = file.read().split('\n\n')

    points = {
        tuple(map(int, x.split(',')))
        for x in points.splitlines()
    }
    instructions = [
        x.removeprefix('fold along ').split('=')
        for x in instructions.splitlines()
    ]
    instructions = [(axis, int(value))for axis, value in instructions]

    rows = max(points, key=lambda x: x[1])[1] + 1
    cols = max(points, key=lambda x: x[0])[0] + 1

    mtx = np.zeros((rows, cols), int)
    for c, r in points:
        mtx[r, c] = 1

    ans1 = part1(mtx, instructions)
    print(f'Answer 1: {ans1}')

    print(f'Answer 2:')
    part2(mtx, instructions)


def fold(mtx, axis, value):
    if axis == 'y':
        base = mtx[:value, :]
        folded = np.flipud(mtx[value + 1:, :])
    elif axis == 'x':
        base = mtx[:, :value]
        folded = np.fliplr(mtx[:, value + 1:])
    mtx = base + folded
    return mtx


def part1(mtx, instructions):
    axis, value = instructions[0]
    mtx = fold(mtx, axis, value)
    return np.sum(mtx > 0)


def part2(mtx, instructions):
    for axis, value in instructions:
        mtx = fold(mtx, axis, value)
    mtx = mtx > 0

    symbols = {True: '▮', False: ' '}
    for r in range(mtx.shape[0]):
        for c in range(mtx.shape[1]):
            print(symbols[mtx[r, c]], end=' ')
        print()
    return None


if __name__ == '__main__':
    main()
