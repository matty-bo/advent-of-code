data = 34000000
N = 900000
tab = [0 for i in range(N)]
for i in range(1, N):
    count = 0
    for e in range(0, N, i):
        if count < 50:
            tab[e] += i*11
            count += 1
        else:
            e += i
tab, N = tab[1:], N-1
index = -1
for i in range(N):
    if tab[i] > data:
        index = i
        break
print('Answer 2:', index+1)