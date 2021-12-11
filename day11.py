def main():
    filename = "inputs/input11"
    with open(filename) as file:
        grid = [
            [int(octopus) for octopus in row]
            for row in file.read().splitlines()
        ]

    ans1 = part1(grid)
    print(f'Answer 1: {ans1}')

    ans2 = part2(grid)
    print(f'Answer 2: {ans2}')


def graph_builder(grid):
    graph = {}

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            possible_neighbours = [
                (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),
                (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)
            ]

            neighbours = [
                (row, col) for row, col in possible_neighbours
                if 0 <= row < len(grid) and 0 <= col < len(grid[0])
            ]
            graph[(r, c)] = {'energy': grid[r][c], 'neighbours': neighbours}
    return graph


def execute_step(graph):
    queue = set()

    # get initial flashes
    for point in graph:
        graph[point]['energy'] += 1
        if graph[point]['energy'] > 9:
            queue.add(point)

    # execute flashes and spread them
    flashed = set()
    flash_count = 0
    while queue:
        point = queue.pop()
        if graph[point]['energy'] <= 9:
            continue

        flash_count += 1
        graph[point]['energy'] = 0
        flashed.add(point)

        for neighbour in graph[point]['neighbours']:
            if neighbour not in flashed:
                graph[neighbour]['energy'] += 1
                queue.add(neighbour)

    return (graph, flash_count)


def part1(grid):
    graph = graph_builder(grid)
    STEPS = 100
    total_flash_count = 0
    for step in range(STEPS):
        graph, flash_count = execute_step(graph)
        total_flash_count += flash_count
    return total_flash_count


def part2(grid):
    graph = graph_builder(grid)
    step = 0
    flash_count = 0
    while flash_count != len(graph):
        graph, flash_count = execute_step(graph)
        step += 1
    return step


if __name__ == '__main__':
    main()
