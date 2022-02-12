def main():
    filename = "inputs/input6"
    with open(filename) as file:
        timers = list(map(int, file.readline().split(',')))
    ans1 = part1(timers)
    ans2 = part2(timers)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')

def part1(timers):
    for _ in range(80):
        new_fishes =  sum([timer == 0 for timer in timers])
        timers = [timer - 1 if timer > 0 else 6 for timer in timers]
        timers += [8] * new_fishes
    ans = len(timers)
    return ans

def part2(timers):
    day_counts = [timers.count(i) for i in range(9)]
    for _ in range(256):
        day_counts = day_counts[1:] + day_counts[:1]
        day_counts[6] += day_counts[-1]
    ans = sum(day_counts)
    return ans

if __name__ == '__main__':
    main()