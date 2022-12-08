from functools import reduce


DIRECTIONS = {
    'left': lambda x, y: (x - 1, y),
    'right': lambda x, y: (x + 1, y),
    'up': lambda x, y: (x, y - 1),
    'down': lambda x, y: (x, y + 1),
}


def main():
    filename = "inputs/input8"
    with open(filename) as file:
        grid = [[int(x) for x in line] for line in file.read().splitlines()]

    points = {}
    row_size, col_size = len(grid), len(grid[0])
    for row in range(row_size):
        for col in range(col_size):
            points[(row, col)] = grid[row][col]

    ans1 = part1(points)
    ans2 = part2(points)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(points):
    col_size = max(points, key=lambda p: p[0])[0] + 1
    row_size = max(points, key=lambda p: p[1])[1] + 1
    ans = 0
    for point in points:
        visibility = {
            'left': True,
            'right': True,
            'up': True,
            'down': True,
        }
        for direction in DIRECTIONS:
            x, y = point
            while 0 < x < col_size - 1 and 0 < y < row_size - 1:
                x, y = DIRECTIONS[direction](x, y)
                if points[(x, y)] >= points[point]:
                    visibility[direction] = False
                    break
        ans += any(visibility.values())
    return ans


def part2(points):
    col_size = max(points, key=lambda p: p[0])[0] + 1
    row_size = max(points, key=lambda p: p[1])[1] + 1

    scores = []
    for point in points:
        visibility = {
            'left': 0,
            'right': 0,
            'up': 0,
            'down': 0,
        }
        for direction in DIRECTIONS:
            x, y = point
            while 0 < x < col_size - 1 and 0 < y < row_size - 1:
                x, y = DIRECTIONS[direction](x, y)
                visibility[direction] += 1
                if points[(x, y)] >= points[point]:
                    break

        score = reduce(lambda a, b: a * b, visibility.values())
        scores.append(score)
    ans = max(scores)
    return ans


if __name__ == '__main__':
    main()
