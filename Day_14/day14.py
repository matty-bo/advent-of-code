def distance(reindeer, time):
    dist, passed = 0, 0
    f, r = 0, 0
    fly = True
    while passed <= time:
        if fly:
            dist += reindeer['speed']
            f += 1
            if f == reindeer['fly']:
                f, fly = 0, False
        elif not fly:
            r += 1
            if r == reindeer['rest']:
                r, fly = 0, True
        passed += 1
    return dist


def points(reindeers, time):
    dp = {r: [0, 0] for r in reindeers}
    passed = 0
    while passed < time:
        max_dist = 0
        for r in dp:
            dp[r][0] = distance(reindeers[r], passed)
            if dp[r][0] > max_dist:
                max_dist = dp[r][0]
        for r in dp:
            if dp[r][0] == max_dist:
                dp[r][1] += 1
        passed += 1
    winner_points = max([dp[r][1] for r in reindeers])
    return winner_points


reindeers = {'Comet': {'speed': 14, 'fly': 10, 'rest': 127},
             'Dancer': {'speed': 16, 'fly': 11, 'rest': 162}}
race_time = 2503
print("Answer 1:", max([distance(reindeers[r], race_time) for r in reindeers]))

rs = {}
filename = 'day14_data.txt'
with open(filename) as file:
    for line in file:
        line = line.strip().split()
        rs[line[0]] = {'speed': int(line[3]),
                       'fly': int(line[6]),
                       'rest': int(line[-2])}
print('Answer 2:', points(rs, race_time))
