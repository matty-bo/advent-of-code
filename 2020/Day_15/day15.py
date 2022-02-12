def speak_nth_number(numbers, n):
    d = {nr: {'last_idx': numbers.index(nr),
              'count': numbers.count(nr)} for nr in numbers}
    spoken = numbers[-1]
    for turn in range(len(numbers), n):
        if d[spoken]['count'] == 1:
            spoken = 0
        elif d[spoken]['count'] > 1:
            spoken = d[spoken]['last_idx'] - d[spoken]['before_idx']
        if spoken in d:
            d[spoken] = {'before_idx': d[spoken]['last_idx'],
                         'last_idx': turn,
                         'count': d[spoken]['count'] + 1}
        else:
            d[spoken] = {'last_idx': turn, 'count': 1}
    return spoken


filename = 'input15.txt'
with open(filename) as file:
    data = file.read().split(',')
numbers = [int(nr) for nr in data]

ans1 = speak_nth_number(numbers, 2020)
print('Answer 1:', ans1)

ans2 = speak_nth_number(numbers, 30_000_000)
print('Answer 2:', ans2)
