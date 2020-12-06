filename = 'input6.txt'
with open(filename) as file:
    data = file.read().split('\n\n')

ans1 = sum(len({char for char in s if char != '\n'}) for s in data)
print('Answer 1:', ans1)

group_sets = [[{ans for ans in answers} for answers in group.split()] for group in data]
everyone = [len(answers[0].intersection(*answers[1:])) for answers in group_sets]
ans2 = sum(everyone)
print('Answer 2:', ans2)
