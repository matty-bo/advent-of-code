from copy import deepcopy
from functools import reduce
import re


MONKEY_INPUT_REGEX = r"""Monkey (\d+):
  Starting items: (.+?)
  Operation: new = old (.+?) (.+?)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""


class Monkey:
    def __init__(self, nr, items, operation, test):
        self.nr = nr
        self.items = items
        self.operation = operation
        self.test = test
        self.thrown_items = 0

    def inspect(self, item):
        arg = self.operation['arg']
        arg = item if arg == 'old' else int(arg)
        new_item = self.operation['func'](item, arg)
        return new_item

    def get_test_result(self, item):
        divisor = self.test['divisor']
        if item % divisor == 0:
            result = self.test['true']
        else:
            result = self.test['false']
        return result

    def play_turn(self, monkeys, part=1):
        items_thrown_in_turn = len(self.items)

        lcm = reduce(lambda x, y: x * y,
                     (monkey.test['divisor']
                      for monkey in monkeys.values())
                     )
        if part == 1:
            def reduce_worry(x): return x // 3
        elif part == 2:
            lcm = reduce(lambda x, y: x * y,
                         (monkey.test['divisor']
                          for monkey in monkeys.values())
                         )

            def reduce_worry(x): return x % lcm
        while self.items:
            item = self.items.pop()
            item = self.inspect(item)
            item = reduce_worry(item)

            test_result = self.get_test_result(item)
            monkeys[test_result].receive(item)

        self.thrown_items += items_thrown_in_turn

    def receive(self, item):
        self.items.append(item)

    def __str__(self):
        return self.nr

    def __repr__(self):
        return f"Monkey {self.nr}"


def parse_monkey(monkey_data):
    monkey_match = re.match(MONKEY_INPUT_REGEX, monkey_data)
    if monkey_match:
        nr = int(monkey_match.group(1))
        items = [
            int(item) for item
            in monkey_match
            .group(2)
            .replace(' ', '')
            .split(',')
        ]
        operation_type = monkey_match.group(3)
        operation_arg = monkey_match.group(4)
        test_divisor = int(monkey_match.group(5))
        test_true = int(monkey_match.group(6))
        test_false = int(monkey_match.group(7))

        if operation_type == '*':
            def operation_func(x, y): return x * y
        elif operation_type == '+':
            def operation_func(x, y): return x + y

        operation = {
            'type': operation_type,
            'arg': operation_arg,
            'func': operation_func,
        }

        test = {
            'divisor': test_divisor,
            'true': test_true,
            'false': test_false,
        }
        return Monkey(nr, items, operation, test)


def main():
    filename = "inputs/input11"
    with open(filename) as file:
        monkeys_input = file.read().split('\n\n')
    monkeys = {}
    for monkey_data in monkeys_input:
        monkey = parse_monkey(monkey_data)
        monkeys[monkey.nr] = monkey

    monkeys1 = deepcopy(monkeys)
    monkeys2 = deepcopy(monkeys)
    ans1 = part1(monkeys1)
    ans2 = part2(monkeys2)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(monkeys):
    round_count = 20
    for round in range(round_count):
        for monkey in monkeys:
            m = monkeys[monkey]
            m.play_turn(monkeys, part=1)
    items_thrown_count = [
        monkey.thrown_items
        for _, monkey in monkeys.items()
    ]

    items_thrown_count = sorted(items_thrown_count)
    monkey_bussiness = reduce(lambda x, y: x * y, items_thrown_count[-2:])
    return monkey_bussiness


def part2(monkeys):

    round_count = 10000
    for round in range(round_count):
        for monkey in monkeys:
            m = monkeys[monkey]
            m.play_turn(monkeys, part=2)

    items_thrown_count = [
        monkey.thrown_items
        for _, monkey in monkeys.items()
    ]

    items_thrown_count = sorted(items_thrown_count)
    monkey_bussiness = reduce(lambda x, y: x * y, items_thrown_count[-2:])
    return monkey_bussiness


if __name__ == '__main__':
    main()
