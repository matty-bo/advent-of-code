
def main():
    filename = "inputs/input2"

    with open(filename) as file:
        commands = list(
            map(lambda x:
                (x.split(' ')[0], int(x.split(' ')[1])),
                file.readlines())
        )
    ans1 = part1(commands)
    ans2 = part2(commands)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def part1(commands):
    moves = {
        'forward': lambda pos, arg:  {
            'depth': pos['depth'],
            'horizontal': pos['horizontal'] + arg
        },
        'down': lambda pos, arg: {
            'depth': pos['depth'] + arg,
            'horizontal': pos['horizontal']
        },
        'up': lambda pos, arg: {
            'depth': pos['depth'] - arg,
            'horizontal': pos['horizontal']
        }
    }

    pos = {'depth': 0, 'horizontal': 0}

    for cmd, arg in commands:
        pos = moves[cmd](pos, arg)

    ans = pos['depth'] * pos['horizontal']

    return ans


def part2(commands):
    pos = {'depth': 0, 'horizontal': 0, 'aim': 0}

    moves = {
        'forward': lambda pos, arg:  {
            'depth': pos['depth'] + pos['aim'] * arg,
            'horizontal': pos['horizontal'] + arg,
            'aim': pos['aim']
        },
        'down': lambda pos, arg: {
            'depth': pos['depth'],
            'horizontal': pos['horizontal'],
            'aim': pos['aim'] + arg
        },
        'up': lambda pos, arg: {
            'depth': pos['depth'],
            'horizontal': pos['horizontal'],
            'aim': pos['aim'] - arg
        }
    }

    for cmd, arg in commands:
        pos = moves[cmd](pos, arg)
    ans = pos['depth'] * pos['horizontal']
    return ans


if __name__ == '__main__':
    main()