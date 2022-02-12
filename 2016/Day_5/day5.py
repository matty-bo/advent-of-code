import hashlib


door = 'ojvtpuvg'

inc, count = 0, 0
ans1 = []
while count < 8:
    indicates = True
    inc = str(inc)
    tohash = (door + inc).encode()
    h = hashlib.md5(tohash).hexdigest()
    for i in range(5):
        if h[i] != '0':
            indicates = False
    if indicates:
        count += 1
        ans1.append(h[5])
    inc = int(inc)
    inc += 1
print('Answer 1:', ''.join(ans1))

ans2 = [None for i in range(8)]
inc, count = 0, 0
while count < 8:
    indicates = True
    inc = str(inc)
    tohash = (door + inc).encode()
    h = hashlib.md5(tohash).hexdigest()
    for i in range(5):
        if h[i] != '0':
            indicates = False
    if indicates:
        if h[5].isdigit():
            if 0 <= int(h[5]) <= 7 and not ans2[int(h[5])]:
                ans2[int(h[5])] = h[6]
                count += 1
    inc = int(inc)
    inc += 1
print('Answer 2:', ''.join(ans2))