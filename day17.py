import re


def main():
    filename = "inputs/input17"
    with open(filename) as file:
        data = file.read()
    coordinates = re.match(r'.+=(.+)\.\.(.+),.+=(.+)\.\.(.+)', data).groups()
    txl, txu, tyl, tyu = (int(c) for c in coordinates)

    ans1, ans2 = both_parts(txl, txu, tyl, tyu)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def both_parts(txl, txu, tyl, tyu):

    pairs = []
    for x in range(0, 2 * txu):
        for y in range(2 * tyl, -tyl):
            pairs.append((x, y))

    heights = {}
    for init_vx, init_vy in pairs:
        x, y = (0, 0)
        vx, vy = init_vx, init_vy
        max_y = 0
        overshoot = False
        while not overshoot:
            if (txl <= x <= txu and tyl <= y <= tyu):
                overshoot = False
                heights[(init_vx, init_vy)] = max_y
                break
            x, y = x + vx, y + vy
            if y > max_y:
                max_y = y
            if vx != 0:
                vx = vx - 1 if vx > 0 else vx + 1
            vy -= 1
            if x > txu or y < tyl:
                overshoot = True
    ans1, ans2 = max(heights.values()), len(heights)
    return ans1, ans2


if __name__ == '__main__':
    main()
