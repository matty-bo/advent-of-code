def new_seq(seq):
    indexes = [[0, seq[0]]]
    for i in range(len(seq) - 1):
        if seq[i] != seq[i + 1]:
            indexes.append([i + 1, seq[i + 1]])
    for i in range(len(indexes)-1):
        indexes[i][0] = str(indexes[i+1][0] - indexes[i][0])
    ind = len(indexes) - 1
    indexes[ind][0] = str(len(seq) - indexes[ind][0])
    new = []
    for p in indexes:
        p = ''.join(p)
        new.append(p)
    return ''.join(new)


seq = '1113122113'
for i in range(50):
    seq = new_seq(seq)
print(len(seq))
