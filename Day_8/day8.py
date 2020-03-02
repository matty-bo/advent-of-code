import re


def print_screen():
    printing = {0: ' ', 1: '#'}
    for i in range(r):
        for j in range(c):
            print(printing[screen[i][j]], end=' ')
        print()
    print()


def rect(x, y):
    for i in range(y):
        for j in range(x):
            screen[i][j] = 1


def row(y, shift):
    screen[y] = screen[y][-shift:] + screen[y][:-shift]


def col(x, shift, y):
    column = [screen[i][x] for i in range(y)]
    new_col = column[-shift:] + column[:-shift]
    for i in range(y):
        screen[i][x] = new_col[i]
    # print(column)

with open('input8.txt') as file:
    data = [line.strip() for line in file]
instructions = []
for line in data:
    inst = re.sub('x',' ',re.sub('rotate |y=|x=|by ','',line)).split()
    instructions.append((inst[0], int(inst[1]), int(inst[2])))
c, r = 50, 6
screen = [[0 for w in range(c)] for h in range(r)]
for i in instructions:
    if i[0] == 'rect':
        rect(i[1], i[2])
    if i[0] == 'row':
        row(i[1], i[2])
    if i[0] == 'column':
        col(i[1], i[2], r)
ans1 = sum([screen[i][j] for i in range(r) for j in range(c)])
print('Answer 1:', ans1)
print('Answer 2:',)
print_screen()
