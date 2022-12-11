STRAIGHT_MOVES = {
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y),
    'U': lambda x, y: (x, y + 1),
    'D': lambda x, y: (x, y - 1),
}

DIAGONAL_MOVES = {
    'RU': lambda x, y: (x + 1, y + 1),
    'LU': lambda x, y: (x - 1, y + 1),
    'RD': lambda x, y: (x + 1, y - 1),
    'LD': lambda x, y: (x - 1, y - 1),
}

MOVES = {
    **STRAIGHT_MOVES,
    **DIAGONAL_MOVES
}


def main():
    filename = "inputs/input9"
    with open(filename) as file:
        moves = [move.split(' ') for move in file.read().splitlines()]
    moves = [(direction, int(steps)) for direction, steps in moves]

    ans1 = part1(moves)
    ans2 = part2(moves)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def adjacent(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if abs(x1 - x2) > 1 or abs(y1 - y2) > 1:
        return False
    return True


def get_next_move(tail, head):
    if tail[0] != head[0] and tail[1] != head[1]:
        for direction in DIAGONAL_MOVES:
            x, y = DIAGONAL_MOVES[direction](*tail)
            if adjacent((x, y), head):
                return direction
    else:
        for direction in STRAIGHT_MOVES:
            x, y = STRAIGHT_MOVES[direction](*tail)
            if adjacent((x, y), head):
                return direction


def part1(moves):
    s = (0, 0)
    T, H = s, s
    visited_points = {T}
    for direction, steps in moves:
        for step in range(1, steps + 1):
            H = MOVES[direction](*H)
            if not adjacent(T, H):
                tail_move = get_next_move(T, H)
                T = MOVES[tail_move](*T)
                visited_points.add(T)
    ans = len(visited_points)
    return ans


def part2(moves):
    s = (0, 0)
    KNOTS_COUNT = 10
    knots = [s for _ in range(KNOTS_COUNT)]
    visited_points = {s}
    for direction, steps in moves:
        for step in range(1, steps + 1):
            for idx in range(len(knots)):
                if idx == 0:
                    knots[idx] = MOVES[direction](*knots[idx])
                else:
                    front_knot_idx = idx - 1
                    if not adjacent(knots[idx], knots[front_knot_idx]):
                        knot_move = get_next_move(
                            knots[idx], knots[front_knot_idx])
                        knots[idx] = MOVES[knot_move](*knots[idx])
                        if idx == KNOTS_COUNT - 1:
                            visited_points.add(knots[idx])
    ans = len(visited_points)
    return ans


if __name__ == '__main__':
    main()
