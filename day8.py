import re

def main():
    filename = "inputs/input8"
    with open(filename) as file:
        displays = [re.match(r'(.*) \| (.*)$', line).groups() for line in file.readlines()]
        displays = [(line[0].split(' '), line[1].split(' ')) for line in displays]
    
    ans1 = part1(displays)
    print(f'Answer 1: {ans1}')
    
    ans2 = part2(displays)
    print(f'Answer 2: {ans2}')

def part1(displays):
    ans = 0
    for inputs, outputs in displays:
        unique_segments_counts = sum([len(signal) in (2, 3, 4, 7) for signal in outputs])
        ans += unique_segments_counts
    return ans

def part2(displays):
    ans = 0
    for inputs, outputs in displays:
        decoder = get_signals_decoder(inputs)
        output_digits = []
        for out in outputs:
            out = ''.join(sorted(out))
            out = str(decoder[out])
            output_digits.append(out)
        output_nr = int(''.join(output_digits))
        ans += output_nr
    return ans
    

def get_signals_decoder(signals):
    decoded = {
        0: None, # len = 6 and len (intersection with 4) = 3
        1: next(set(s) for s in signals if len(s) == 2),
        2: None, # left
        3: None, # len = 5 and letters in (one)
        4: next(set(s) for s in signals if len(s) == 4),
        5: None, # len = 5 and len (intersection with 6) = 5
        6: None, # len = 6 and left
        7: next(set(s) for s in signals if len(s) == 3),
        8: next(set(s) for s in signals if len(s) == 7),
        9: None, # len = 6 and len(intersection with 1) = 2
    }

    length_five_signals = [set(s) for s in signals if len(s) == 5]
    length_six_signals = [set(s) for s in signals if len(s) == 6]

    decoded[3] = next(s for s in length_five_signals if s & decoded[1] == decoded[1])
    length_five_signals.remove(decoded[3])

    decoded[0] = next(s for s in length_six_signals if len(s & decoded[3]) == 4 and len(s & decoded[1]) == 2)
    length_six_signals.remove(decoded[0])

    decoded[9] = next(s for s in length_six_signals if len(s & decoded[1]) == 2)
    length_six_signals.remove(decoded[9])

    decoded[6] = length_six_signals[0]

    decoded[5] = next(s for s in length_five_signals if len(s & decoded[6]) == 5)
    length_five_signals.remove(decoded[5])

    decoded[2] = length_five_signals[0]

    decoded = {
        ''.join(sorted(sig)): dig 
        for dig, sig in decoded.items()
    }
    return decoded

if __name__ == '__main__':
    main()