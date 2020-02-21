import re

def cut_cards(n, deck):
    if n > 0:
        for i in range(n):
            deck.append(deck.pop(0))
    elif n < 0:
        for i in range(-n):
            deck.insert(0, deck.pop())
    return deck


def deal_increment(n, deck):
    new_deck = [None for i in range(len(deck))]
    i = 0
    while None in new_deck and deck:
        new_deck[i] = deck.pop(0)
        i += n
        if i > len(new_deck):
            i %= len(new_deck)
    return new_deck


filename = 'day22_data.txt'
data = []
with open(filename) as file:
    for line in file.readlines():
        data.append(line)
deck = [i for i in range(10007)]

moves = []
for shuffle in data:
    if re.search('deal with increment', shuffle):
        x = re.search(r"\s(\w+)$|\s-(\w+)$", shuffle)
        moves.append(['dwi', int(x.group()[1:])])
    elif re.search('cut', shuffle):
        x = re.search(r"\s(\w+)$|\s-(\w+)$", shuffle)
        moves.append(['cut', int(x.group()[1:])])
    elif re.search('deal into new stack', shuffle):
        moves.append(['dins'])

for m in moves:
    if m[0] == 'dins':
        deck.reverse()
    if m[0] == 'cut':
        deck = cut_cards(m[1], deck)
    if m[0] == 'dwi':
        deck = deal_increment(m[1], deck)

print("Answer 1:",deck.index(2019))
