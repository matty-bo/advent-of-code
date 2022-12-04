
def main():
    filename = "inputs/input3"
    with open(filename) as file:
        backpacks = [line.strip() for line in file.readlines()]
    backpacks_compartments = [
        (b[:len(b) // 2], b[len(b) // 2:]) for b in backpacks]

    ans1 = part1(backpacks_compartments)
    ans2 = part2(backpacks)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def calculate_item_priority(item_type):
    LOWERCASE_ASCII_OFFSET = 96
    UPPERCASE_ASCII_OFFSET = 38
    item_ascii_code = ord(item_type)
    ascii_offset = LOWERCASE_ASCII_OFFSET if item_type.islower() else UPPERCASE_ASCII_OFFSET
    item_priority = item_ascii_code - ascii_offset
    return item_priority


def part1(backpacks_compartments):
    ans = 0
    for compartment_1, compartment_2 in backpacks_compartments:
        compartments_product = set(compartment_1) & set(compartment_2)
        common_item_type = compartments_product.pop()
        ans += calculate_item_priority(common_item_type)
    return ans


def part2(backpacks):
    ans = 0
    elf_groups = [backpacks[i: i + 3] for i in range(0, len(backpacks), 3)]
    for group in elf_groups:
        elf_1, elf_2, elf_3 = group
        groups_product = set(elf_1) & set(elf_2) & set(elf_3)
        badge = groups_product.pop()
        ans += calculate_item_priority(badge)
    return ans


if __name__ == '__main__':
    main()
