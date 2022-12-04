def main():
    filename = "inputs/input4"
    with open(filename) as file:
        assignment_pairs = [line.strip().split(',')
                            for line in file.readlines()]

    def parse_assignment(assignment):
        return tuple(
            int(digit)
            for digit
            in assignment.split('-')
        )
    assignment_pairs = [
        (
            parse_assignment(assignment_1),
            parse_assignment(assignment_2)
        )
        for (assignment_1, assignment_2)
        in assignment_pairs
    ]
    ans1 = part1(assignment_pairs)
    ans2 = part2(assignment_pairs)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(assignment_pairs):
    ans = 0
    for pair in assignment_pairs:
        assignment_1, assignment_2 = pair
        assignment_1_start, assignment_1_end = assignment_1
        assignment_2_start, assignment_2_end = assignment_2

        if assignment_1_start >= assignment_2_start and assignment_1_end <= assignment_2_end:
            ans += 1
        elif assignment_2_start >= assignment_1_start and assignment_2_end <= assignment_1_end:
            ans += 1
    return ans


def part2(assignment_pairs):
    ans = 0
    for pair in assignment_pairs:
        assignment_1, assignment_2 = pair
        assignment_1_sections = set(
            range(
                assignment_1[0],
                assignment_1[1] + 1
            )
        )
        assignment_2_sections = set(
            range(
                assignment_2[0],
                assignment_2[1] + 1
            )
        )
        overlapping_sections = assignment_1_sections & assignment_2_sections
        ans += len(overlapping_sections) > 0
    return ans


if __name__ == '__main__':
    main()
