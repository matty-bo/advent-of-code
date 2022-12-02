MOVES_CODES = {
    'A': 'ROCK',
    'X': 'ROCK',
    'B': 'PAPER',
    'Y': 'PAPER',
    'C': 'SCISSORS',
    'Z': 'SCISSORS',
}

MOVES = {
    'ROCK': {'WIN': 'SCISSORS', 'LOSE': 'PAPER'},
    'PAPER': {'WIN': 'ROCK', 'LOSE': 'SCISSORS'},
    'SCISSORS': {'WIN': 'PAPER', 'LOSE': 'ROCK'},
}

SHAPE_SCORES = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}

EXPECTED_RESULT = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}


def main():
    filename = "inputs/input2"
    with open(filename) as file:
        rounds_strategies = [line.split() for line in file.readlines()]

    ans1 = part1(rounds_strategies)
    ans2 = part2(rounds_strategies)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def calculate_player_round_score(player_move, enemy_move):
    player_score = None
    if player_move == enemy_move:
        player_score = 3
    elif MOVES[player_move]['LOSE'] == enemy_move:
        player_score = 0
    elif MOVES[player_move]['WIN'] == enemy_move:
        player_score = 6
    player_score += SHAPE_SCORES[player_move]
    return player_score


def part1(round_strategies):
    ans = 0
    for round in round_strategies:
        enemy_move, your_move = MOVES_CODES[round[0]], MOVES_CODES[round[1]]
        round_score = calculate_player_round_score(your_move, enemy_move)
        ans += round_score
    return ans


def determine_move(enemy_move, expected_result):
    if expected_result == 'DRAW':
        return enemy_move
    elif expected_result == 'WIN':
        return MOVES[enemy_move]['LOSE']
    elif expected_result == 'LOSE':
        return MOVES[enemy_move]['WIN']


def part2(round_strategies):
    ans = 0
    for round in round_strategies:
        enemy_move, expected_result = MOVES_CODES[round[0]
                                                  ], EXPECTED_RESULT[round[1]]
        your_move = determine_move(enemy_move, expected_result)
        round_score = calculate_player_round_score(your_move, enemy_move)
        ans += round_score
    return ans


if __name__ == '__main__':
    main()
