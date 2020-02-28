row, column = 2978, 3083
mul, div = 252533, 33554393
code = 20151125
d = row + column - 1
op_count = int(d*(d+1)/2) - row
for i in range(op_count):
    code = (code * mul) % div
print('Answer:', code)
