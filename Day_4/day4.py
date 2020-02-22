import hashlib

data = 'ckczppom'
ans1 = 0
found = False
while not found:
    result = hashlib.md5((data + str(ans1)).encode()).hexdigest()
    if result[:5] == '00000':
        print("Answer 1:", ans1)
        found = True
    ans1 += 1

ans2 = 0
found = False
while not found:
    result = hashlib.md5((data + str(ans2)).encode()).hexdigest()
    if result[:6] == '000000':
        print("Answer 2:", ans2)
        found = True
    ans2 += 1
