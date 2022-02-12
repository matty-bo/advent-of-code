def nice_string(string):
    count = 0
    for char in string:
        if char in 'aeiou':
            count += 1
        if count > 3:
            break
    if count < 3:
        return False
    nice = False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            nice = True
            break
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in string:
            nice = False
    return nice


def nicer(string):
    nice = False
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            nice = True
            break
    if not nice:
        return nice
    nice = False
    for i in range(len(string)-1):
        pair = string[i] + string[i+1]
        for j in range(i+2, len(string)-1):
            pair2 = string[j] + string[j+1]
            if pair == pair2:
                nice = True
    return nice


filename = 'day5_data.txt'
data = []
with open(filename) as file:
    for line in file:
        data.append(line)
ans1 = 0
for string in data:
    if nice_string(string):
        ans1 += 1
ans2 = 0
for string in data:
    if nicer(string):
        ans2 += 1
print('Answer 1:', ans1)
print('Answer 2:', ans2)
