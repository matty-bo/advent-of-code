class Robot:
    def __init__(self):
        self.x,  self.y = 0, 0
        self.direction = 0
    def turn(self, t):
        if t == 0:
            t = -1
        self.direction = (self.direction + t) % 4
    def move(self):
        move_x,  move_y = {1: -1, 3: 1}, {0: 1, 2: -1}
        if self.direction in move_x:
            self.x += move_x[self.direction]
        elif self.direction in move_y:
            self.y += move_y[self.direction]

def ga(modes, ip, shift, rel_base):
    if modes[-shift] == "0":
        return memory[ip + shift]
    elif modes[-shift] == "1":
        return ip + shift
    elif modes[-shift] == "2":
        return memory[ip + shift] + rel_base

def computer(memory, points, ip=0, fp=1):
    rel_base = 0
    output = []
    robot = Robot()
    camera = 0
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] + memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 2:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] * memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 3:
            if fp == 0:
                points[robot.x, robot.y] = 1
                fp += 1
            if points.get((robot.x, robot.y)) is None:
                points[robot.x, robot.y] = 0
            if points[robot.x, robot.y] == 0:
                camera = 0
            elif points[robot.x, robot.y] == 1:
                camera = 1
            memory[ga(modes, ip, 1, rel_base)] = camera
        elif op_code == 4:
            output.append(memory[ga(modes, ip, 1, rel_base)])
            if len(output) == 2:
                points[robot.x, robot.y] = output[0]
                robot.turn(output[1])
                robot.move()
                output = []
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
            return
        if op_code in [1, 2, 7, 8]:
            ip += 4
        elif op_code in [3, 4, 9]:
            ip += 2

def draw_grid(points):
    w = min(p[0] for p in points) - 1
    h = min(p[1] for p in points) - 1
    obj = {0: ' ', 1: '█'}
    for j in range(0, h, -1):
        for i in range(0, w, -1):
            try:
                print(obj[points[i, j]], end='')
            except:
                print(end=' ')
        print()

filename = "day11_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
for i in range(len(memory) * 10):
    memory.append(0)
points = {}
computer(memory, points)
print("Task 1: %d" % len(points))
points2 = {}
print("Task 2:")
computer(memory, points2, 0, 0)
draw_grid(points2)
