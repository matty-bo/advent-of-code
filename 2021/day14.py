from collections import Counter


def main():
    filename = "inputs/input14"
    with open(filename) as file:
        polymer, rules = file.read().split('\n\n')

    polymer = polymer.strip()
    rules = [tuple(x.split(' -> ')) for x in rules.splitlines()]
    rules = {(key[0], key[1]): val for key, val in rules}

    ans1 = part1(polymer, rules)
    print(f'Answer 1: {ans1}')

    ans2 = part2(polymer, rules)
    print(f'Answer 2: {ans2}')


def part1(polymer, rules):
    polymer = [l for l in polymer]
    for step in range(10):
        i = 0
        while i < len(polymer):
            rule = tuple(polymer[i: i+2])
            if rule in rules:
                polymer.insert(i + 1, rules[rule])
                i += 1
            i += 1
    pairs_count = Counter(polymer)
    mx = max(pairs_count.values())
    mn = min(pairs_count.values())
    return mx - mn


def part2(polymer, rules):
    letters_count = Counter(polymer)
    pairs_count = Counter()

    for i in range(len(polymer)):
        rule = tuple(polymer[i: i+2])
        if rule in rules:
            pairs_count[rule] += 1

    for step in range(40):
        temp_pairs_count = Counter({k: v for k, v in pairs_count.items()})
        pairs_count.clear()

        for r in rules:
            if r in temp_pairs_count:
                pairs_count[(r[0], rules[r])] += temp_pairs_count[r]
                pairs_count[(rules[r], r[1])] += temp_pairs_count[r]

                letters_count[rules[r]] += temp_pairs_count[r]

    mx = max(letters_count.values())
    mn = min(letters_count.values())
    return  mx - mn


if __name__ == '__main__':
    main()
