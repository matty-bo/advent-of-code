filename = 'day8_data.txt'
ans1, ans2 = 0, 0
with open(filename) as file:
    for line in file:
        ans1 += len(line.strip()) - len(eval(line.strip()))
        ans2 += line.strip().count('\\') + line.strip().count('"') + 2
print('Answer 1:', ans1)
print('Answer 2:', ans2)
