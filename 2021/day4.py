
def main():
    filename = "inputs/input4"

    with open(filename) as file:
        data = file.read().split('\n\n')

    draw_order = list(map(int, data[0].split(',')))
    boards = [
        [list(map(int, fields.split())) for fields in board.split('\n')]
        for board in data[1:]
    ]

    ans1 = part1(draw_order, boards)
    ans2 = part2(draw_order, boards)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')

def part1(draw_order, boards):

    def get_winning_board(boards, drawn):
        for j in range(len(boards)):
            has_won = check_board_win(boards[j], drawn)
            if has_won:
                return boards[j]
        return None
    
    winning_board = None
    turns = 0
    for i in range(len(draw_order)):
        winning_board = get_winning_board(boards, draw_order[:i])
        if winning_board:
            turns = i
            break

    marked = draw_order[:turns]
    sum_unmarked = sum(
        sum(nr for nr in row if nr not in marked)
        for row in winning_board
    )
    ans = sum_unmarked * draw_order[turns - 1]
    return ans


def part2(draw_order, boards):
    
    last_winning_board = None
    turns = 0

    winning_boards = {idx for idx in range(len(boards)) if check_board_win(boards[idx], draw_order)}
    for i in range(len(draw_order), 0, -1):
        now_winning_boards = {j for j in range(len(boards)) if check_board_win(boards[j], draw_order[:i])}
        if len(now_winning_boards) < len(winning_boards):
            last_winning_board_idx = (winning_boards - now_winning_boards).pop()
            turns = i
            break

    last_winning_board = boards[last_winning_board_idx]

    marked = draw_order[:turns + 1]
    sum_unmarked = sum(
        sum(nr for nr in row if nr not in marked)
        for row in last_winning_board
    )
    ans = sum_unmarked * draw_order[turns]
    return ans

def check_board_win(board, drawn):
    for row in board:
        if all(nr in drawn for nr in row):
            return True
    t_board = list(zip(*board))
    for row in t_board:
        if all(nr in drawn for nr in row):
            return True
    return False

if __name__ == '__main__':
    main()
