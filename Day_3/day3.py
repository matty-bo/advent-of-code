import math


class LineSegment:

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "[(%d,%d) (%d,%d)]" % (self.x1, self.y1, self.x2, self.y2)


def create_segment(x2p, y2p, instruction):
    segment = LineSegment()
    segment.x1 = x2p
    segment.y1 = y2p
    if instruction[0] == 'R':
        segment.x2 = segment.x1 + int(instruction[1:len(instruction)])
        segment.y2 = y2p
    elif instruction[0] == 'L':
        segment.x2 = segment.x1 - int(instruction[1:len(instruction)])
        segment.y2 = y2p
    elif instruction[0] == 'U':
        segment.x2 = x2p
        segment.y2 = segment.y1 + int(instruction[1:len(instruction)])
    elif instruction[0] == 'D':
        segment.x2 = x2p
        segment.y2 = segment.y1 - int(instruction[1:len(instruction)])
    return segment


def create_wire(data1):
    wire = [create_segment(0, 0, data1[0])]
    for i in range(1, len(data1)):
        wire.append(create_segment(wire[i-1].x2, wire[i-1].y2, data1[i]))
    return wire


# orientation - returns:
# 0 if horizontal
# 1 if vertical
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


# creates crosspoints list for task 2
def append_cross_point(seg1, seg2, cross_points):
    # seg1 needs to be horizontal, seg2 needs to be vertical
    if orientation(seg1) == 1 and orientation(seg2) == 0:
        seg1, seg2 = seg2, seg1

    # adjusting segment to check conditions
    adjust_segment(seg1)
    adjust_segment(seg2)
    if (seg1.x1 <= seg2.x1 <= seg1.x2) and (seg2.y1 <= seg1.y1 <= seg2.y2):
        if seg2.x1 != 0 and seg1.y1 != 0:
            cross_points.append(str(seg2.x1) + "," + str(seg1.y1))  # creates list of cross points needed for task 2


def create_cross_list(wire1, wire2, cross_points):
    output_list = []
    for i in wire1:
        for j in wire2:
            append_cross_point(i, j, cross_points)
    for point in cross_points:
        pair = point.split(sep=",")
        pair = list(map(int, pair))
        output_list.append(pair)
    return output_list


def manhattan_distance(wire1, wire2, cross_points):
    minn = -1
    for point in cross_points:
        distance = int(math.fabs(point[0]) + math.fabs(point[1]))
        if 0 < distance < minn:
            minn = distance
        if minn == -1:
            minn = distance
    return minn


#TASK 2 FUNCTIONS
def segment_length(x1,y1,x2,y2):
    return int(math.sqrt((x2-x1)**2+(y2-y1)**2))


def cross_distance(wire, xi, yi):
    total = 0
    for seg in wire:
        if seg.y1 == yi == seg.y2:
            if seg.x1 <= xi <= seg.x2 or seg.x2 <= xi <= seg.x1:
                total += segment_length(xi, yi, seg.x1, seg.y1)
                return total
        elif seg.y1 == seg.y2:
            total += int(math.fabs(seg.x2 - seg.x1))
        if seg.x1 == xi == seg.x2:
            if seg.y1 <= yi <= seg.y2 or seg.y2 <= yi <= seg.y1:
                total += segment_length(xi, yi, seg.x1, seg.y1)
                return total
        elif seg.x1 == seg.x2:
            total += int(math.fabs(seg.y2 - seg.y1))
    return total


def closest_cross_sum(wire3, wire4, cross_points):
    minn = -1
    d1 = 0
    d2 = 0
    for point in cross_points:
        d2 = cross_distance(wire3, int(point[0]), int(point[1]))
        d1 = cross_distance(wire4, int(point[0]), int(point[1]))
        if d1+d2 < minn:
            minn = d1+d2
        if minn == -1:
            minn = d1+d2
    return minn


def answer():
    filename = "day3_data.txt"
    with open(filename) as file:
        data1 = file.readline()
        data2 = file.readline()

    data1 = data1.split(',')
    data2 = data2.split(',')

    wire1 = create_wire(data1)
    wire2 = create_wire(data2)

    wire3 = create_wire(data1)
    wire4 = create_wire(data2)
    cross_points = []
    cross_points = create_cross_list(wire1, wire2, cross_points)
    print("Task 1:", manhattan_distance(wire1, wire2, cross_points))
    print("Task 2:", closest_cross_sum(wire3, wire4, cross_points))


answer()
