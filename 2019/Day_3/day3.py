import math

class LineSegment:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def create_segment(x2p, y2p, instruction):
    segment = LineSegment(x2p, y2p)
    direction, length = instruction[0], int(instruction[1:])
    dir_x, dir_y = {"L": -1, "R": 1, "D": 0, "U": 0}, {"L": 0, "R": 0, "D": -1, "U": 1}
    if dir_y[direction] == 0:
        segment.x2 = segment.x1 + dir_x[direction] * length
        segment.y2 = y2p
    if dir_x[direction] == 0:
        segment.x2 = x2p
        segment.y2 = segment.y1 + dir_y[direction] * length
    return segment

def create_wire(data):
    wire = [create_segment(0, 0, data[0])]
    for i in range(1, len(data)):
        wire.append(create_segment(wire[i-1].x2, wire[i-1].y2, data[i]))
    return wire

def orientation(seg):
    if seg.y1 == seg.y2:
        return 0  # horizontal
    if seg.x1 == seg.x2:
        return 1  # vertical
    return -1

# adjusts segments to meet conditions of correct work of find_cross() function
def adjust_segment(seg):
    if seg.x1 == seg.x2 and seg.y1 > seg.y2:
        seg.y1, seg.y2 = seg.y2, seg.y1
    if seg.y1 == seg.y2 and seg.x1 > seg.x2:
        seg.x1, seg.x2 = seg.x2, seg.x1
    return seg

def get_cross_point(seg1, seg2):
    # seg1 needs to be horizontal, seg2 needs to be vertical
    if orientation(seg1) == 1 and orientation(seg2) == 0:
        seg1, seg2 = seg2, seg1
    # adjusting segment to check conditions
    adjust_segment(seg1), adjust_segment(seg2)
    if (seg1.x1 <= seg2.x1 <= seg1.x2) and (seg2.y1 <= seg1.y1 <= seg2.y2):
        if seg2.x1 != 0 and seg1.y1 != 0:
            return [seg2.x1, seg1.y1]
    return None

def create_cross_list(wire1, wire2):
    cross_points = []
    for i in wire1:
        for j in wire2:
            point = get_cross_point(i, j)
            if point:
                cross_points.append(point)
    return cross_points

def manhattan_distance(cross_points):
    minn = -1
    for point in cross_points:
        distance = int(math.fabs(point[0]) + math.fabs(point[1]))
        if 0 < distance < minn or minn == -1:
            minn = distance
    return minn

#TASK 2 FUNCTIONS
def segment_length(x1, y1, x2, y2):
    return int(math.sqrt((x2-x1)**2+(y2-y1)**2))

def point_distance(wire, xi, yi):
    total = 0
    for seg in wire:
        if seg.y1 == yi == seg.y2:
            if seg.x1 <= xi <= seg.x2 or seg.x2 <= xi <= seg.x1:
                total += segment_length(xi, yi, seg.x1, seg.y1)
                return total
        elif seg.y1 == seg.y2:
            total += int(math.fabs(seg.x2 - seg.x1))
        if  seg.x1 == xi == seg.x2:
            if seg.y1 <= yi <= seg.y2 or seg.y2 <= yi <= seg.y1:
                total += segment_length(xi, yi, seg.x1, seg.y1)
                return total
        elif seg.x1 == seg.x2:
            total += int(math.fabs(seg.y2 - seg.y1))
    return total

def closest_cross_sum(wire1, wire2, cross_points):
    minn = -1
    for point in cross_points:
        d1 = point_distance(wire1, point[0], point[1])
        d2 = point_distance(wire2, point[0], point[1])
        if d1+d2 < minn or minn == -1:
            minn = d1+d2
    return minn

filename = "day3_data.txt"
with open(filename) as file:
    data1, data2 = file.readline().split(','), file.readline().split(',')
wire1, wire2 = create_wire(data1), create_wire(data2)
wire3, wire4 = create_wire(data1), create_wire(data2)
cross_points = create_cross_list(wire1, wire2)
print("Task 1:", manhattan_distance(cross_points))
print("Task 2:", closest_cross_sum(wire3, wire4, cross_points))