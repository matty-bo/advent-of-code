import re
from copy import deepcopy


def main():
    filename = "inputs/input5"
    with open(filename) as file:
        crates_input, procedure = file.read().split('\n\n')
        crates_input = crates_input.split('\n')
        procedure = procedure.split('\n')

    stack_numbers = list(map(int, crates_input[-1].split()))
    crates_input = [
        l.replace('    ', ' [x]').replace(
            '[', '').replace(']', '').replace(' ', '')
        for l in crates_input[:-1]
    ]

    stacks = {stack: [] for stack in stack_numbers}
    for line in crates_input[::-1]:
        for i in range(len(line)):
            crate = line[i]
            if crate != 'x':
                stacks[i + 1].append(crate)

    steps = []
    for line in procedure:
        line = line.strip()
        match_step = re.match('move (\d+) from (\d+) to (\d+)', line)
        step = {}
        step['quantity'], step['from'], step['to'] = map(
            int, match_step.groups())
        steps.append(step)

    initial_stacks = deepcopy(stacks)
    ans1 = part1(initial_stacks, steps)
    initial_stacks = deepcopy(stacks)
    ans2 = part2(initial_stacks, steps)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(stacks, steps):
    for step in steps:
        quantity = step['quantity']
        source = step['from']
        destination = step['to']

        for _ in range(quantity):
            moving_crate = stacks[source].pop()
            stacks[destination].append(moving_crate)
    ans = ""
    for stack_nr in sorted(stacks):
        top_crate = stacks[stack_nr][-1]
        ans += top_crate

    return ans


def part2(stacks, steps):
    for step in steps:
        quantity = step['quantity']
        source = step['from']
        destination = step['to']

        moving_crates = stacks[source][-quantity:]
        stacks[destination] += moving_crates
        stacks[source] = stacks[source][:-quantity]

    ans = ""
    for stack_nr in sorted(stacks):
        top_crate = stacks[stack_nr][-1]
        ans += top_crate

    return ans


if __name__ == '__main__':
    main()
