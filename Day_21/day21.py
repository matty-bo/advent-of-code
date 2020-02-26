import itertools


def attack(a, d):
    dmg_dealt = a['DMG'] - d['Armor']
    if dmg_dealt < 1:
        dmg_dealt = 1
    d['HP'] -= dmg_dealt


def fight(me, boss):
    attack(me, boss)
    if boss['HP'] <= 0:
        return me['name']
    attack(boss, me)
    if me['HP'] <= 0:
        return boss['name']
    return None


# cost, dmg, armor
weapons = [     # one weapon only
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]
armor = [      # 0 or 1 armor
    [0, 0, 0],
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5]
]
rings = [       # 0, 1 or 2 rings
    [0, 0, 0],
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3]
]

equipment = []
war_help = list(itertools.product(weapons, armor, rings, rings))
war = [list(line) for line in war_help]
for line in war:
    if line[-1] == line[-2]:
        line.remove(line[-2])
cda = []
for line in war:
    c, d, a = 0, 0, 0
    for el in line:
        c += el[0]
        d += el[1]
        a += el[2]
    cda.append([c, d, a])
cda.sort(key=lambda x: x[0])
boss = {'name': 'Boss', 'HP': 109, 'DMG': 8, 'Armor': 2}
me = {'name': 'Me', 'HP': 100, 'DMG': 0, 'Armor': 0}

cost1, eq_id = 0, 0
winner = None
while winner != 'Me':
    cost1, me['DMG'], me['Armor'] = cda[eq_id][0], cda[eq_id][1], cda[eq_id][2]
    winner = None
    while not winner:
        winner = fight(me, boss)
    me['HP'], boss['HP'] = 100, 109
    eq_id += 1
print('Answer 1:', cost1)

cost2, eq_id = 0, 0
cda.sort(key=lambda x: x[0], reverse=True)
while winner != 'Boss':
    cost2, me['DMG'], me['Armor'] = cda[eq_id][0], cda[eq_id][1], cda[eq_id][2]
    winner = None
    while not winner:
        winner = fight(me, boss)
    me['HP'], boss['HP'] = 100, 109
    eq_id += 1
print('Answer 2:', cost2)
