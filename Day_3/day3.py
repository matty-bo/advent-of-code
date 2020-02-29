def split_lengths(v, l):
    for i in range(0,len(v), l):
        yield v[i:i+l]

def triangles(data):
    count = 0
    for a, b, c in data:
        if a + b > c and a + c > b and b + c > a:
            count += 1
    return count

with open('input3.txt') as file:
    data = [list(map(int, line.split())) for line in file]
ans1 = triangles(data)
print('Answer 1:', ans1)

joined_columns = [length[0] for length in data] + [length[1] for length in data] + [length[2] for length in data]
ans2 = triangles(split_lengths(joined_columns, 3))
print('Answer 2:', ans2)

