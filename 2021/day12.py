START, END = 'start', 'end'


def main():
    filename = "inputs/input12"
    with open(filename) as file:
        tunnels = list(
            map(
                lambda x: x.strip().split('-'),
                file.readlines()
            )
        )

    graph = graph_builder(tunnels)
    visited = set([START])

    ans1 = dfs(graph, START, visited)
    print(f'Answer 1: {ans1}')

    ans2 = dfs(graph, START, visited, True)
    print(f'Answer 2: {ans2}')


def graph_builder(tunnels):
    graph = {}
    for v1, v2 in tunnels:
        graph[v1] = graph.get(v1, []) + [v2]
        graph[v2] = graph.get(v2, []) + [v1]
    return graph


def dfs(graph, node, visited, visit_twice=False):
    if node == END:
        return 1

    path_count = 0
    for neighbour in graph[node]:
        if neighbour.isupper():
            path_count += dfs(graph, neighbour, visited, visit_twice)
        else:
            if neighbour not in visited:
                new_visited = set(visited) | set([neighbour])
                path_count += dfs(graph, neighbour, new_visited, visit_twice)
            elif visit_twice and neighbour not in (START, END):
                path_count += dfs(graph, neighbour, visited, False)

    return path_count


if __name__ == '__main__':
    main()
