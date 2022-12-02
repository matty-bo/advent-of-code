def main():
    filename = "inputs/input1"
    with open(filename) as file:
        inventories = file.read().split('\n\n')

    inventories = list(map(lambda inventory: [int(
        calories) for calories in inventory.split()], inventories))
    ans1 = part1(inventories)
    ans2 = part2(inventories)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(inventories):
    most_nutritious_inventory = max(inventories, key=sum)
    ans = sum(most_nutritious_inventory)
    return ans


def part2(inventories):
    inventories_calories = [sum(inventory) for inventory in inventories]
    top_3_most_nutritious_inventories = sorted(
        inventories_calories, reverse=True)[:3]
    ans = sum(top_3_most_nutritious_inventories)
    return ans


if __name__ == '__main__':
    main()
