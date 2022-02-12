filename = 'input12.txt'
with open(filename) as file:
    data = [(way[0], int(way[1:])) for way in file.readlines()]

actions = {'N': lambda x, y, val: (x, y + val),
           'S': lambda x, y, val: (x, y - val),
           'E': lambda x, y, val: (x + val, y),
           'W': lambda x, y, val: (x - val, y),
           'L': lambda angle: (angle + val) % 360,
           'R': lambda angle: (angle - val) % 360,
           'F': lambda x, y, val, angle: actions[ways[angle]](x, y, val)}

ways = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

ship_x, ship_y, ship_angle = 0, 0, 0
for way, val in data:
    if way in ['N', 'S', 'E', 'W']:
        ship_x, ship_y = actions[way](ship_x, ship_y, val)
    elif way in ['L', 'R']:
        ship_angle = actions[way](ship_angle)
    elif way == 'F':
        ship_x, ship_y = actions[way](ship_x, ship_y, val, ship_angle)
ans1 = abs(ship_x) + abs(ship_y)
print('Answer 1:', ans1)

ship_x, ship_y = 0, 0
wp_x, wp_y = 10, 1
cos = {0: 1, 90: 0, 180: -1, 270: 0}
sin = {0: 0, 90: 1, 180: 0, 270: -1}
for way, val in data:
    if way in ['N', 'S', 'E', 'W']:
        wp_x, wp_y = actions[way](wp_x, wp_y, val)
    elif way == 'L':
        wp_x, wp_y = (cos[val] * wp_x - sin[val] * wp_y), (sin[val] * wp_x + cos[val] * wp_y)
    elif way == 'R':
        val = 360 - val
        wp_x, wp_y = (cos[val] * wp_x - sin[val] * wp_y), (sin[val] * wp_x + cos[val] * wp_y)
    elif way == 'F':
        ship_x, ship_y = (ship_x + val * wp_x), (ship_y + val * wp_y)

ans2 = abs(ship_x) + abs(ship_y)
print('Answer 2:', ans2)
