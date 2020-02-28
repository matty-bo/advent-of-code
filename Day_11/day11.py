def decode(password):
    return ''.join([chr(x) for x in password])


def increment(p, size):
    while p[size - 1] +1 == 123:
        p[size - 1] = 97
        size -= 1
    p[size-1] += 1
    return p


def has_three(password):
    if len(password) < 3:
        return False
    for i in range(len(password)-2):
        if p[i+1] == p[i] + 1 and p[i+2] == p[i] + 2:
            return True
    return False


def forbidden_letters(password):
    return any(char in [105, 108, 111] for char in password)


def two_pairs(password):
    p = password.copy()
    count = 0
    for i in range(len(p)-1):
        if p[i] == p[i+1] and p[i] != 0:
            p[i], p[i+1] = 0, 0
    return p.count(0) >= 4


def valid_password(p):
    if has_three(p) and two_pairs(p) and not forbidden_letters(p):
        return True
    return False


old = 'cqjxjnds'
size = len(old)
p = [ord(char) for char in old]

while not valid_password(p):
    p = increment(p, len(p))
print('Answer 1:', decode(p))

p = increment(p, len(p))
while not valid_password(p):
    p = increment(p, len(p))
print('Answer 2:', decode(p))






