def main():
    filename = "inputs/input3"

    with open(filename) as file:
        numbers = file.read().splitlines()
    ans1 = part1(numbers)
    ans2 = part2(numbers)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(numbers):
    numbers = list(zip(*numbers))

    zeros_count = [sum(bit == '0' for bit in nr) for nr in numbers]
    ones_count = [sum(bit == '1' for bit in nr) for nr in numbers]
    both_counts = list(zip(zeros_count, ones_count))

    gamma_rate = [str(count.index(max(count))) for count in both_counts]
    epsilon_rate = [str(count.index(min(count))) for count in both_counts]

    gamma_rate = int(''.join(gamma_rate), 2)
    epsilon_rate = int(''.join(epsilon_rate), 2)

    ans = gamma_rate * epsilon_rate
    return ans


def part2(numbers):

    def compute_criteria_bit(rate_name, zeros_count, ones_count):
        if rate_name == 'oxygen_rate':
            return 1 if ones_count == zeros_count else int(
                zeros_count < ones_count)
        elif rate_name == 'co2_rate':
            return 0 if ones_count == zeros_count else int(
                zeros_count > ones_count)
        return None

    def get_rate_index(numbers, rate_name):
        numbers = list(zip(*numbers))
        discarded = set()

        for col in numbers:
            zeros_count = sum(
                col[i] == '0' and i not in discarded
                for i in range(len(col))
            )
            ones_count = sum(
                col[i] == '1' and i not in discarded
                for i in range(len(col))
            )

            criteria_bit = compute_criteria_bit(
                rate_name, zeros_count, ones_count
            )

            to_discard = [
                i for i in range(len(col))
                if col[i] != str(criteria_bit)
            ]

            discarded.update(to_discard)
            if(len(col) - len(discarded) == 1):
                break

        all_indices = set(range(len(numbers[0])))
        idx_set = all_indices - discarded
        idx = idx_set.pop()
        return idx

    oxygen_rate = numbers[get_rate_index(numbers, 'oxygen_rate')]
    co2_rate = numbers[get_rate_index(numbers, 'co2_rate')]
    ans = int(oxygen_rate, 2) * int(co2_rate, 2)
    return ans


if __name__ == '__main__':
    main()
