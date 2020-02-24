import re


def spoon_combinations():
    res = []
    for i in range(100):
        for j in range(100 - i):
            for k in range(100 - i - j):
                h = 100 - i - j - k
                res.append([i, j, k, h])
    return res


def cookie_score(spoons, recipes):
    cp = {'capacity': 0,
          'durability': 0,
          'flavor': 0,
          'texture': 0,
          'calories': 0}
    for ing in spoons:
        for r in recipes[ing]:
            try:
                cp[r] += spoons[ing] * recipes[ing][r]
            except:
                pass
    score = 1
    if cp['calories'] != 500:
        return 0
    for p in cp:
        if cp[p] < 0:
            return 0
        if p != 'calories':
            score *= cp[p]
    return score


filename = 'day15_data.txt'
recipes = {}
with open(filename) as file:
    for line in file:
        line = re.sub('[,:]', '', line).strip().split()
        recipes[line[0]] = {line[1]: int(line[2]),
                            line[3]: int(line[4]),
                            line[5]: int(line[6]),
                            line[7]: int(line[8]),
                            line[9]: int(line[10])}
spoons = {ing: 0 for ing in recipes}
best_score = 0
for c in spoon_combinations():
    spoons['Sugar'] = c[0]
    spoons['Sprinkles'] = c[1]
    spoons['Candy'] = c[2]
    spoons['Chocolate'] = c[3]
    score = cookie_score(spoons, recipes)
    best_score = max(score, best_score)
print('Answer 2:', best_score)
