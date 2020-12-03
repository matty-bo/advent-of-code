def count_trees(array, right_nr, down_nr):
    cols = len(array[0])
    j = 0
    count = 0
    for i in range(0, len(array), down_nr):
        count += array[i][j] == '#'
        j += right_nr
        if j >= cols:
            j %= cols
    return count


filename = 'input3.txt'
with open(filename) as file:
    data = list(map(lambda x: x.rstrip(), file.readlines()))

ans1 = count_trees(data, 3, 1)
print('Answer 1:', ans1)

rd_slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
ans2 = 1
for slope in rd_slopes:
    ans2 *= count_trees(data, slope[0], slope[1])
print('Answer 2:', ans2)

