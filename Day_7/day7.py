def has_shiny(curr, bags):
    if not bags[curr]:
        return False
    if 'shiny gold' in bags[curr]:
        return True
    else:
        for bag in bags[curr]:
            if has_shiny(bag, bags):
                return True
    return False


def count_inside(curr, bags):
    if curr == 'shiny gold':
        count = 0
    else:
        count = 1
    if not bags[curr]:
        return 1
    else:
        for bag in bags[curr]:
            count += bags[curr][bag] * count_inside(bag, bags)
    return count


filename = 'input7.txt'
with open(filename) as file:
    data = list(map(lambda s: s.replace(' bags contain ', ', ').split(', '), file.readlines()))

bags = {bag_info[0]: {' '.join(bag.split()[1:3]): int(bag.split()[0])
                      for bag in bag_info[1:]
                      if bag.split()[0] != 'no'}
        for bag_info in data}

ans1 = sum(has_shiny(bag, bags) for bag in bags)
print('Answer 1:', ans1)

ans2 = count_inside('shiny gold', bags)
print('Answer 2:', ans2)
