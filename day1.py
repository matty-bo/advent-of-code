def main():
    filename = "inputs/input1"
    with open(filename) as file:
        numbers = list(map(int, file.readlines()))
    ans1 = part1(numbers)
    ans2 = part2(numbers)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')

def part1(numbers):
    ans = sum(numbers[idx] < numbers[idx + 1] for idx in range(len(numbers) - 1))
    return ans

def part2(numbers):
    window_sums = [sum(numbers[idx: idx + 3]) for idx in range(len(numbers) - 2)]
    ans = sum(window_sums[idx] < window_sums[idx + 1]
           for idx in range(len(window_sums) - 1))
    return ans

if __name__ == '__main__':
    main()