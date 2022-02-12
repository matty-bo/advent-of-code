def main():
    filename = "inputs/input7"
    with open(filename) as file:
        positions = list(map(int, file.readline().split(',')))

    ans1 = part1(positions)
    print(f'Answer 1: {ans1}')

    ans2 = part2(positions)
    print(f'Answer 2: {ans2}')

def part1(positions):
    min_pos, max_pos = min(positions), max(positions)
    min_abs_dist = float('inf')
    for pos in range(min_pos, max_pos + 1):
        abs_dist = sum(abs(crab - pos) for crab in positions)
        if abs_dist < min_abs_dist:
            min_abs_dist = abs_dist
    ans = min_abs_dist
    return ans


def calc_fuel(steps, fuel=0):
    if steps == 0:
        return fuel
    else:
        return fuel + calc_fuel(steps - 1, fuel + 1)


def part2(positions):
    min_pos, max_pos = min(positions), max(positions)
    min_fuel = float('inf')
    for pos in range(min_pos, max_pos + 1):
        abs_distances = [abs(crab - pos) for crab in positions]
        fuel = sum(d * (d+1) // 2 for d in abs_distances)
        if fuel < min_fuel:
            min_fuel = fuel
    ans = min_fuel
    return ans


if __name__ == '__main__':
    main()
