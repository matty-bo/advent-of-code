with open('input2.txt') as file:
    data = [line.strip() for line in file]

keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
r, c = 1, 1
move = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

buttons = []
for line in data:
    for way in line:
        if 0 <= r + move[way][0] <= 2:
            r += move[way][0]
        if 0 <= c + move[way][1] <= 2:
            c += move[way][1]
    buttons.append(str(keypad[r][c]))
ans1 = ''.join(buttons)
print('Answer 1:', ans1)


keypad2 = [['0', '0', '1', '0', '0'],
           ['0', '2', '3', '4', '0'],
           ['5', '6', '7', '8', '9'],
           ['0', 'A', 'B', 'C', '0'],
           ['0', '0', 'D', '0', '0']]
buttons2 = []
r, c = 2, 0
for line in data:
    for way in line:
        if 0 <= r + move[way][0] <= 4 and 0 <= c + move[way][1] <= 4:
            if keypad2[r+move[way][0]][c+move[way][1]] != '0':
                r += move[way][0]
                c += move[way][1]
    buttons2.append(keypad2[r][c])
ans2 = ''.join(buttons2)
print('Answer 2:', ans2)