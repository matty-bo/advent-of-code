def binary_search(s, li, start, end):
    mid = (start + end) // 2
    if li == len(s):
        return start
    if s[li] in ['F', 'L']:
        return binary_search(s, li + 1, start, mid - 1)
    elif s[li] in ['B', 'R']:
        return binary_search(s, li + 1, mid + 1, end)


filename = 'input5.txt'
with open(filename) as file:
    data = list(map(str.strip, file.readlines()))

seats = []
for x in data:
    r = binary_search(x[:7], 0, 0, 127)
    c = binary_search(x[-3:], 0, 0, 7)
    seat_id = r * 8 + c
    seats.append(seat_id)
ans1 = max(seats)
print('Answer 1:', ans1)

ans2 = -1
for s in range(ans1):
    if not s - s % 8 in [0, 127] and s not in seats:
        ans2 = s
print('Answer 2:', ans2)
