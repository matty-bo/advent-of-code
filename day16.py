def main():
    filename = "inputs/input16"
    with open(filename) as file:
        hex = file.read()
    byte_array = [hex[i: i + 2] for i in range(0, len(hex), 2)]

    bits = ''.join([hex_to_bits(byte) for byte in byte_array])

    _, _, ver_sums, ans2 = parse_bits(bits)
    
    ans1 = sum(ver_sums)
    print(f'Answer 1: {ans1}')
    print(f'Answer 2: {ans2}')


def hex_to_bits(hex_byte):
    return str(bin(int(hex_byte, base=16)))[2:].zfill(8)


def bits_to_int(bits):
    return int(bits, base=2)


def parse_literal(bits):
    bits_count = 0
    while True:
        bits_count += 5
        if bits[bits_count - 5] == '0':
            break
    literal = bits[:bits_count]
    literal = ''.join([literal[i] for i in range(len(literal)) if i % 5 != 0])
    literal = bits_to_int(literal)
    return (literal, bits_count)


def parse_bits(bits, i=0):
    ver_sums = []
    vals = []
    version, type = bits[i: i + 3], bits[i + 3: i + 6]
    ver_sums.append(bits_to_int(version))
    i += 6

    if type == '100':
        val, bits_count = parse_literal(bits[i:])
        i += bits_count
        vals.append(val)
    else:
        if bits[i] == '1':
            subpackets = bits_to_int(bits[i + 1: i + 12])
            i += 12
            ver_sum = 0
            for _ in range(subpackets):
                version, next_i, vs, val = parse_bits(bits, i)
                i = next_i
                ver_sum += sum(vs)
                vals.append(val)
            ver_sums.append(ver_sum)
        else:
            length_in_bits = bits_to_int(bits[i + 1: i + 16])
            i += 16
            end_i = i + length_in_bits
            ver_sum = 0
            while i < end_i:
                version, next_i, vs, val = parse_bits(bits, i)
                i = next_i
                ver_sum += sum(vs)
                vals.append(val)
            ver_sums.append(ver_sum)

    type = bits_to_int(type)
    match type:
        case 0:
            val = sum(vals)
        case 1:
            val = 1
            for v in vals:
                val = val * v
        case 2:
            val = min(vals)
        case 3:
            val = max(vals)
        case 5:
            val = vals[0] > vals[1]
        case 6:
            val = vals[0] < vals[1]
        case 7:
            val = vals[0] == vals[1]

    return version, i, ver_sums, val 


if __name__ == '__main__':
    main()
