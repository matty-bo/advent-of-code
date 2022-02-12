from queue import PriorityQueue


def main():
    filename = "inputs/input15"
    with open(filename) as file:
        matrix = [
            [int(risk) for risk in row]
            for row in file.read().splitlines()
        ]

    ans1 = djikstra(matrix)
    print(f'Answer 1: {ans1}')

    ans2 = djikstra(matrix, rep=5)
    print(f'Answer 2: {ans2}')


def djikstra(matrix, rep=1):
    start, end = (0, 0), (rep * len(matrix) - 1, len(rep * matrix[0]) - 1)
    D = {start: 0}
    D[start] = 0

    Q = PriorityQueue()
    Q.put((0, start))
    while not Q.empty():
        _, v = Q.get()
        for n, risk in get_neighbours(v, matrix, rep):
            if n not in D or D[v] + risk < D[n]:
                D[n] = D[v] + risk
                Q.put((D[n], n))

    return D[end]


def get_new_risk(risk, idx):
    return (risk - 1 + idx) % 9 + 1


def get_neighbours(v, matrix, rep):
    r, c = v
    old_m, old_n = len(matrix), len(matrix[0])
    m, n = rep * old_m, rep * old_n

    possible_neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for nr, nc in possible_neighbours:
        if 0 <= nr < m and 0 <= nc < n:
            risk = get_new_risk(
                matrix[nr % old_m][nc % old_n],
                nr // old_m + nc // old_n
            )
            yield (nr, nc), risk


if __name__ == '__main__':
    main()
