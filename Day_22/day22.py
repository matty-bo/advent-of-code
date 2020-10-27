import re


filename = 'day22_data.txt'
data = []
with open(filename) as file:
    for line in file.readlines():
        data.append(line)

moves = []
for move in data:
    if re.search('deal with increment', move):
        x = re.search(r"\s(\w+)$|\s-(\w+)$", move)
        moves.append(['dwi', int(x.group()[1:])])
    elif re.search('cut', move):
        x = re.search(r"\s(\w+)$|\s-(\w+)$", move)
        moves.append(['cut', int(x.group()[1:])])
    elif re.search('deal into new stack', move):
        moves.append(['dins'])

def shuffle(moves, ds):
    a, b = 1, 0
    for m in moves:
        if m[0] == 'dins':
            a, b = -a % ds, (-b - 1) % ds
        elif m[0] == 'cut':
            a, b = a % ds, (b - m[1]) % ds
        elif m[0] == 'dwi':
            a, b = (a * m[1]) % ds, (b * m[1]) % ds
    return a, b

card = 2019
ds = 10007
a, b = shuffle(moves, ds)
ans1 = (a * card + b) % ds
print(f'Card {card} is at: &{ans1}')

N = 101741582076661
ds = 119315717514047
pos = 2020
a, b = shuffle(moves, ds)
r = (b * pow(1-a, ds-2, ds)) % ds
print(f"Card at &{pos}: {((pos - r) * pow(a, N*(ds-2), ds) + r) % ds}")
