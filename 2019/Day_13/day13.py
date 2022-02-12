import math

def ga(modes, ip, shift, rel_base):
    if modes[-shift] == "0":
        return memory[ip + shift]
    elif modes[-shift] == "1":
        return ip + shift
    elif modes[-shift] == "2":
        return memory[ip + shift] + rel_base

def computer(memory, points, ip=0):
    rel_base = 0
    output = []
    x_ball, x_paddle = 0, 0
    final_score = 0
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] + memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 2:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] * memory[ga(modes, ip, 2, rel_base)]

        elif op_code == 3:      # Inputs
            #draw_grid(points)
            if x_ball - x_paddle != 0:
                joystick = math.copysign(1, x_ball - x_paddle)
            else:
                joystick = 0
            memory[ga(modes, ip, 1, rel_base)] = joystick

        elif op_code == 4:      # Outputs
            output.append(memory[ga(modes, ip, 1, rel_base)])
            if len(output) == 3:
                if output[0] == -1 and output[1] == 0:
                    #print("SCORE:", output[2])
                    final_score = output[2]
                else:
                    if output[2] == 4:  # Ball
                        x_ball = output[0]
                    if output[2] == 3:  # Paddle
                        x_paddle = output[0]
                    points[output[0], output[1]] = output[2]
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
            return final_score
        if op_code in [1, 2, 7, 8]:
            ip += 4
        elif op_code in [3, 4, 9]:
            ip += 2

def draw_grid(points):
    w = max(p[0] for p in points) + 1
    h = max(p[1] for p in points) + 1
    obj = {0: ' ', 1: '@', 2: '#', 3: '_', 4: 'O'}
    for j in range(h):
        for i in range(w):
            try:
                print(obj[points[i, j]], end='')
            except:
                print(" ", end='')
        print()

filename = "day13_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
for i in range(len(memory) * 10):
    memory.append(0)

points = {}
memory[0] = 2
print("Final Score: %d" % computer(memory, points))