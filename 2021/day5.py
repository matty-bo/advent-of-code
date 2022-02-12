import re


def main():
    filename = "inputs/input5"

    lines = []
    with open(filename) as file:
        for line in file:
            coords = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
            coords = tuple(map(int, coords.groups()))
            lines.append(coords)

    ans1 = part1(lines)
    ans2 = part2(lines)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(lines):
    covered_points = {}
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                covered_points[(x1, y)] = covered_points.get((x1, y), 0) + 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                covered_points[(x, y1)] = covered_points.get((x, y1), 0) + 1
    ans = sum(count >= 2 for count in covered_points.values())
    return ans


def part2(lines):
    covered_points = {}
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                covered_points[(x1, y)] = covered_points.get((x1, y), 0) + 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                covered_points[(x, y1)] = covered_points.get((x, y1), 0) + 1
        else:
            a = (y2 - y1)/(x2 - x1)
            b = y1 - a*x1
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                y = a*x + b
                covered_points[(x, y)] = covered_points.get((x, y), 0) + 1

    ans = sum(count >= 2 for count in covered_points.values())
    return ans


if __name__ == '__main__':
    main()
