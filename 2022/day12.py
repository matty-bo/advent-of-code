NEIGHBOURS = {
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y),
    'U': lambda x, y: (x, y + 1),
    'D': lambda x, y: (x, y - 1),
}


def main():
    filename = "inputs/input12"
    with open(filename) as file:
        grid = [[letter for letter in line]
                for line in file.read().splitlines()]

    row_count, col_count = len(grid), len(grid[0])
    S, E = None, None
    start_nodes = []
    for r in range(row_count):
        for c in range(col_count):
            point_elevation = grid[r][c]
            if point_elevation == 'S':
                grid[r][c] = 'a'
                S = (r, c)
            elif grid[r][c] == 'E':
                grid[r][c] = 'z'
                E = (r, c)

            if grid[r][c] == 'a':
                start_nodes.append((r, c))

    for r in range(row_count):
        for c in range(col_count):
            point_elevation = grid[r][c]
            if point_elevation in ('S', 'a'):
                grid[r][c] = 'a'
                start_nodes.append((r, c))
            elif grid[r][c] == 'E':
                grid[r][c] = 'z'

    ans1 = part1(grid, S, E)
    ans2 = part2(grid, start_nodes, E)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def get_reachable_neighbours_going_up(point, grid):
    neighbours = []
    r, c = point

    for get_neighbour_point in NEIGHBOURS.values():
        y, x = get_neighbour_point(r, c)
        if not(0 <= y < len(grid) and 0 <= x < len(grid[0])):
            continue

        if ord(grid[y][x]) - ord(grid[r][c]) <= 1:
            neighbours.append((y, x))
    return neighbours


def dijkstra(graph, start_node, destination_node):
    distances = {point: float('inf') for point in graph}
    distances[start_node] = 0
    unvisited = set(graph.keys())

    current_node = start_node
    while current_node != destination_node and len(unvisited) > 0:
        for neighbour in graph[current_node]:
            if neighbour in unvisited:
                current_distance = distances[current_node] + 1
                if current_distance < distances[neighbour]:
                    distances[neighbour] = current_distance
        if current_node in unvisited:
            unvisited.remove(current_node)
        current_node = min(unvisited, key=lambda x: distances[x])
    return distances[destination_node]


def part1(grid, start_node, destination_node):
    row_count, col_count = len(grid), len(grid[0])
    graph = {}
    for r in range(row_count):
        for c in range(col_count):
            reachable_neighbours = get_reachable_neighbours_going_up(
                (r, c), grid)
            graph[(r, c)] = reachable_neighbours
    ans = dijkstra(graph, start_node, destination_node)
    return ans


def get_reachable_neighbours_going_down(point, grid):
    neighbours = []
    r, c = point

    for get_neighbour_point in NEIGHBOURS.values():
        y, x = get_neighbour_point(r, c)
        if not(0 <= y < len(grid) and 0 <= x < len(grid[0])):
            continue

        if ord(grid[r][c]) - ord(grid[y][x]) <= 1:
            neighbours.append((y, x))
    return neighbours


def dijkstra_all_distances(graph, start_node):
    distances = {point: float('inf') for point in graph}
    distances[start_node] = 0
    unvisited = set(graph.keys())

    current_node = start_node
    while len(unvisited) > 0:
        for neighbour in graph[current_node]:
            if neighbour in unvisited:
                current_distance = distances[current_node] + 1
                if current_distance < distances[neighbour]:
                    distances[neighbour] = current_distance
        if current_node in unvisited:
            unvisited.remove(current_node)
            if len(unvisited) == 0:
                break
        current_node = min(unvisited, key=lambda x: distances[x])
    return distances


def part2(grid, start_nodes, destination_node):
    row_count, col_count = len(grid), len(grid[0])
    graph = {}

    for r in range(row_count):
        for c in range(col_count):
            reachable_neighbours = get_reachable_neighbours_going_down(
                (r, c), grid)
            graph[(r, c)] = reachable_neighbours
    distances = dijkstra_all_distances(graph, destination_node)
    best_start_point = min(start_nodes, key=lambda x: distances[x])
    ans = distances.get(best_start_point, None)
    return ans


if __name__ == '__main__':
    main()
