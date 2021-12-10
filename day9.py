def main():
    filename = "inputs/input9"
    with open(filename) as file:
        heightmap = [
            [int(height) for height in row]
            for row in file.read().splitlines()
        ]

    all_points = {}
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            all_points[(i, j)] = heightmap[i][j]

    ans1 = part1(all_points)
    print(f'Answer 1: {ans1}')

    ans2 = part2(all_points)
    print(f'Answer 2: {ans2}')


def get_low_points(all_points):
    return [point for point in all_points if is_low_point(point, all_points)]


def is_low_point(point, all_points):
    point_height = all_points[point]
    neighbours = get_neighbours(point, all_points)
    is_low = all(point_height < all_points[p] for p in neighbours)
    return is_low


def get_neighbours(point, all_points):
    r, c = point
    possible_neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    neighbours = [n for n in possible_neighbours if n in all_points]
    return neighbours


def basin_size(low_point, all_points):
    basin_size = 0
    visited = set()

    queue = [low_point]
    while queue:
        point = queue.pop()

        neighbours = get_neighbours(point, all_points)

        for n in neighbours:
            if n not in visited and all_points[n] < 9:
                basin_size += 1
                visited.add(n)
                queue.append(n)

    return basin_size


def part1(all_points):
    return sum(all_points[point] + 1 for point in get_low_points(all_points))


def part2(all_points):
    low_points = get_low_points(all_points)
    basin_sizes = [basin_size(point, all_points) for point in low_points]
    s1, s2, s3 = sorted(basin_sizes)[::-1][:3]
    ans = s1 * s2 * s3
    return ans


if __name__ == '__main__':
    main()
