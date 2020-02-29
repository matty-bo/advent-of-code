import random


def print_stats(who):
    print(f'- Player has {player["HP"]} hit points, {player["Armor"]} armor, {player["MP"]} mana')
    print(f'- Boss has {boss["HP"]} hit points')


def print_effects(spell):
    if spell == 'Poison':
        print(f"Poison deals {spells[spell]['Dmg']} damage; it's timer is now {timer[spell]}")
    if spell == 'Shield':
        print(f"{spell}'s timer is now {timer[spell]}")
    if spell == 'Recharge':
        print(f"{spell} provides {spells[spell]['Mana']} mana; its timer is now {timer[spell]}")


def boss_turn():
    # print('---Boss Turn---')
    # print_stats('Boss')
    effects()
    if boss['HP'] <= 0:
        return False
    dmg_dealt = boss['Dmg'] - player['Armor']
    if dmg_dealt < 1:
        dmg_dealt = 1
    player['HP'] -= dmg_dealt
    # print(f'Boss attacks for {dmg_dealt}')
    if player['HP'] <= 0:
        return True
    return False


def player_turn(spell):
    # print('---Player Turn---')
    # print_stats('Player')
    effects()
    # player['HP'] -= 1
    # if player['HP'] <= 0:
    #     return False
    if boss['HP'] <= 0:
        return True
    if not cast_spell(spell):
        return False
    if boss['HP'] <= 0:
        return True
    return False


def effects():
    for spell in timer:
        if timer[spell] > 0:
            apply_spell(spell)
            timer[spell] -= 1
            # print_effects(spell)


def apply_spell(spell):
    boss['HP'] -= spells[spell]['Dmg']
    if timer['Shield'] > 0:
        player['Armor'] = spells['Shield']['Armor']
    else:
        player['Armor'] = 0
    player['HP'] += spells[spell]['Heal']
    player['MP'] += spells[spell]['Mana']


def cast_spell(spell):
    if spells[spell]['MP'] > player['MP']:
        return False
    if spell in ['Missile', 'Drain']:
        player['MP'] -= spells[spell]['MP']
        apply_spell(spell)
    else:
        if timer[spell] > 0:
            return False
        elif timer[spell] == 0:
            player['MP'] -= spells[spell]['MP']
            timer[spell] = spells[spell]['Duration']
    # print(f'- Player casts {spell}')
    return True


spells = {
    'Missile': {'MP': 53, 'Dmg': 4, 'Armor': 0, 'Heal': 0, 'Mana': 0, 'Duration': 0},
    'Drain': {'MP': 73, 'Dmg': 2, 'Armor': 0, 'Heal': 2, 'Mana': 0, 'Duration': 0},
    'Shield': {'MP': 113, 'Dmg': 0, 'Armor': 7, 'Heal': 0, 'Mana': 0, 'Duration': 6},
    'Poison': {'MP': 173, 'Dmg': 3, 'Armor': 0, 'Heal': 0, 'Mana': 0, 'Duration': 6},
    'Recharge': {'MP': 229, 'Dmg': 0, 'Armor': 0, 'Heal': 0, 'Mana': 101, 'Duration': 5}
}

used = []
min_cost = 100000
for i in range(300000):
    game_cost = 0
    timer = {'Shield': 0, 'Poison': 0, 'Recharge': 0}
    boss = {'name': 'Boss', 'HP': 58, 'Dmg': 9}
    player = {'name': 'Player', 'HP': 50, 'MP': 500, 'Armor': 0}
    q = []
    while True:
        spell = random.choice(list(spells))
        if player_turn(spell):
            game_cost += spells[spell]['MP']
            break
        game_cost += spells[spell]['MP']
        q.append(spell)
        if boss_turn():
            break
    q.append(game_cost)
    used.append(q)
    if game_cost < min_cost and player['HP'] > 0:
        min_cost = game_cost

print('Answer 1:', min_cost)
