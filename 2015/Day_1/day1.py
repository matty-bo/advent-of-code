filename = 'day1_data.txt'
with open(filename) as file:
    data = file.read()

floor = 0
moves = {'(': 1, ')': -1}
count = 1
basement = []
for char in data:
    floor += moves.get(char)
    if floor == -1:
        basement.append(count)
    count += 1
print('Answer 1:', floor)
print('Answer 2:', basement[0])


