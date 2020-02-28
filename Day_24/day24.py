from itertools import combinations


def qe(group, size):
    if size == 0:
        return 1
    return group[size-1] * qe(group, size-1)


filename = 'day24_data.txt'
with open(filename) as file:
    data = [int(number.strip()) for number in file.readlines()]
numbers = [i for i in data]
group_weight = int(sum(data) / 3)
first_group = [list(c) for c in combinations(data, 6) if sum(c) == group_weight]
ans1 = 0
print('Answer 1:', qe(first_group[0], len(first_group[0])))

group_weight = int(sum(data) / 4)
first_group = [list(c) for c in combinations(data, 5) if sum(c) == group_weight]
print('Answer 2:', qe(first_group[0], len(first_group[0])))
