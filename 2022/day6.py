def main():
    filename = "inputs/input6"
    with open(filename) as file:
        signal = file.read()
    ans1 = part1(signal)
    ans2 = part2(signal)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(signal):
    ans = None
    marker_length = 4
    for i in range(0, len(signal) - marker_length):
        potential_marker = signal[i: i + marker_length]
        if len(set(potential_marker)) == marker_length:
            ans = i + marker_length
            break
    return ans


def part2(signal):
    ans = None
    marker_length = 14
    for i in range(0, len(signal) - marker_length):
        potential_marker = signal[i: i + marker_length]
        if len(set(potential_marker)) == marker_length:
            ans = i + marker_length
            break
    return ans


if __name__ == '__main__':
    main()
