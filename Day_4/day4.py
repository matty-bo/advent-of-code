filename = 'input4.txt'
with open(filename) as file:
    data = file.read().split('\n\n')
data = [p.replace('\n', ' ').split() for p in data]

passports = [{f.split(':')[0]: f.split(':')[1] for f in p} for p in data]
req_fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

ans1, ans2 = 0, 0
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for p in passports:
    fields = list(p.keys())
    if 'cid' in fields:
        fields.remove('cid')
    valid = sorted(fields) == req_fields
    ans1 += valid
    valid2 = True
    if valid:
        if not 1920 <= int(p['byr']) <= 2002:
            valid2 = False
        if not 2010 <= int(p['iyr']) <= 2020:
            valid2 = False
        if not 2020 <= int(p['eyr']) <= 2030:
            valid2 = False
        if 'cm' in p['hgt'] or 'in' in p['hgt']:
            v, u = int(p['hgt'][:-2]), p['hgt'][-2:]
            if u == 'cm':
                if not 150 <= v <= 193:
                    valid2 = False
            elif u == 'in':
                if not 59 <= v <= 76:
                    valid2 = False
        else:
            valid2 = False
        if not p['hcl'][0] == '#' and len(p['hcl']) != 7:
            valid2 = False
        if p['ecl'] not in eye_colors:
            valid2 = False
        if len(p['pid']) != 9:
            valid2 = False
        ans2 += valid2

print('Answer 1:', ans1)
print('Answer 2:', ans2)

# for p in passports:
#     print(p)
