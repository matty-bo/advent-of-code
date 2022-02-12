data = 34000000
data = int(data/10)
N = 800000
tab = [0 for i in range(N)]
for i in range(1, N):
    for e in range(0, N, i):
        tab[e] += i
tab, N = tab[1:], N-1
index = -1
for i in range(N):
    if tab[i] > data:
        index = i
        break
print('Answer 1:', index+1)
