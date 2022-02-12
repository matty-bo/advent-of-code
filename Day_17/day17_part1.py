def ga(modes, ip, shift, rel_base):
    if modes[-shift] == "0":
        return memory[ip + shift]
    elif modes[-shift] == "1":
        return ip + shift
    elif modes[-shift] == "2":
        return memory[ip + shift] + rel_base

def computer(memory, grid,user_input=0, ip=0):
    rel_base = 0
    row = []
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] + memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 2:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] * memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 3:
            memory[ga(modes, ip, 1, rel_base)] = user_input
        elif op_code == 4:
            out = memory[ga(modes, ip, 1, rel_base)]
            if out != 10:
                row.append(out)
            elif out == 10:
                grid.append(row)
                row = []
        elif op_code == 5:
            if memory[ga(modes, ip, 1, rel_base)] != 0:
                ip = memory[ga(modes, ip, 2, rel_base)]
            else:
                ip += 3
        elif op_code == 6:
            if memory[ga(modes, ip, 1, rel_base)] == 0:
                ip = memory[ga(modes, ip, 2, rel_base)]
            else:
                ip += 3
        elif op_code == 7:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] < memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 8:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] == memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 9:
            rel_base += memory[ga(modes, ip, 1, rel_base)]
        else:
            assert op_code == 99
            return grid
        if op_code in [1, 2, 7, 8]:
            ip += 4
        elif op_code in [3, 4, 9]:
            ip += 2

def get_intersections(scaffolds):
    ans = []
    for point in scaffolds:
        neighbours = [(point[0] - 1, point[1]),
                      (point[0] + 1, point[1]),
                      (point[0], point[1] - 1),
                      (point[0], point[1] + 1)]
        boolean = True
        for n in neighbours:
            if n not in scaffolds:
                boolean = False
        if boolean:
            ans.append(point)
    return ans

def scaffold_points(grid):
    points = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 35:
                points.append((i, j))
    return points

def ans1(points):
    align_sum = 0
    for p in points:
        align_sum += p[0] * p[1]
    return align_sum

filename = "day17_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
for i in range(len(memory) * 10):
    memory.append(0)
grid = []
computer(memory, grid)
scaffolds = scaffold_points(grid)
intersections = get_intersections(scaffolds)
print("Answer 1: ", ans1(intersections))
