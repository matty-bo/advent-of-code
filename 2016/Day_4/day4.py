import re


def real_room(room):
    index = room.index('[')
    id = int(re.search('\d+', room).group())
    s, c = re.sub('-|\d', '', room[:index]), room[index + 1:-1]
    occ = {}
    for letter in s:
        if letter not in occ:
            occ[letter] = 0
        occ[letter] += 1
    decr = [(letter, occ[letter]) for letter in occ]
    decr.sort(key=lambda x: (-x[1], x[0]))
    valid_checksum = ''.join([l for l, c in decr[:5]])
    if valid_checksum == c:
        return id
    return 0

def decrypt(room):
    id = int(re.search('\d+', room).group())
    encrypted, _ = re.split('-\d+', room)
    decrypted = []
    for char in encrypted:
        if char != '-':
            dc = ord(char) + id % 26
            if dc > 122:
                dc -= 26
            decrypted.append(chr(dc))
        else:
            decrypted.append(' ')
    decrypted = ''.join(decrypted)
    return (id, decrypted)

with open('input4.txt') as file:
    rooms = [room.strip() for room in file]
ans1 = 0
for room in rooms:
    ans1 += real_room(room)
print('Answer 1:', ans1)

decrypted_rooms = [decrypt(room) for room in rooms]
ans2 = 0
for room in decrypted_rooms:
    if re.search('north', room[1]):
        ans2 = room[0]
print('Answer 2:', ans2)
