
from collections import deque
from functools import reduce

OPENING_BRACKETS = ('(', '[', '{', '<')
CLOSING_BRACKETS = (')', ']', '}', '>')

BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>', }
SCORES_1 = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
SCORES_2 = {')': 1, ']': 2, '}': 3, '>': 4, None: 0}


def main():
    filename = "inputs/input10"
    with open(filename) as file:
        lines = list(map(str.strip, file.readlines()))

    ans1 = part1(lines)
    print(f'Answer 1: {ans1}')

    ans2 = part2(lines)
    print(f'Answer 2: {ans2}')


def illegal_character(line):
    queue = deque()
    for char in line:
        if char in OPENING_BRACKETS:
            queue.append(char)
        elif char in CLOSING_BRACKETS:
            last_opened = queue.pop()
            if char != BRACKETS[last_opened]:
                return char
    return None


def part1(lines):
    ans = sum(SCORES_1[illegal_character(line)] for line in lines)
    return ans


def get_closure(line):
    queue = deque()
    for char in line:
        if char in OPENING_BRACKETS:
            queue.appendleft(char)
        elif char in CLOSING_BRACKETS:
            queue.popleft()
    closure = ''.join(BRACKETS[b] for b in queue)
    return closure


def part2(lines):
    incomplete_lines = [
        line for line in lines
        if illegal_character(line) is None
    ]

    closures = [get_closure(line) for line in incomplete_lines]

    scores = []
    for closure in closures:
        bracket_points = [SCORES_2[bracket] for bracket in closure]
        score = reduce(
            lambda acc, score: 5 * acc + score,
            bracket_points
        )
        scores.append(score)

    scores = sorted(scores)
    ans = scores[len(scores) // 2]
    return ans


if __name__ == '__main__':
    main()
