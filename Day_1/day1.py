def binary_search(array, el, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == el:
        return mid
    elif el < array[mid]:
        return binary_search(array, el, start, mid - 1)
    elif el > array[mid]:
        return binary_search(array, el, mid + 1, end)


filename = 'input1'
with open(filename) as file:
    data = sorted(list(map(lambda x: int(x.strip()), file.readlines())))
year = 2020
numbers = (-1, -1)
for i in range(len(data)):
    first = data[i]
    second = year - first
    second_idx = binary_search(data, second, 0, len(data) - 1)
    if second_idx not in [-1, i]:
        numbers = (first, second)
ans = numbers[0] * numbers[1]
print('Answer 1:', ans)

numbers2 = (-1, -1, -1)
for i in range(len(data)):
    first = data[i]
    sum_23 = year - first
    for j in range(len(data)):
        if j == i:
            continue
        second = data[j]
        third = sum_23 - second
        third_idx = binary_search(data, third, 0, len(data) - 1)
        if third_idx not in [-1, i, j]:
            numbers2 = (first, second, third)
ans2 = numbers2[0] * numbers2[1] * numbers2[2]
print('Answer 2:', ans2)
