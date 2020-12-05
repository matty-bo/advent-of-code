import re


filename = 'input4.txt'
with open(filename) as file:
    data = file.read().split('\n\n')
data = [p.replace('\n', ' ').split() for p in data]

passports = [{f.split(':')[0]: f.split(':')[1] for f in p} for p in data]
req_fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

ans1, ans2 = 0, 0
for p in passports:
    fields = list(p.keys())
    if 'cid' in fields:
        fields.remove('cid')
    valid = sorted(fields) == req_fields
    ans1 += valid
    valid2 = True
    if valid:
        if not re.fullmatch(r'19[2-9][0-9]|200[0-2]', p['byr']):
            valid2 = False
        if not re.fullmatch(r'20(1[0-9]|20)', p['iyr']):
            valid2 = False
        if not re.fullmatch(r'20(2[0-9]|30)', p['eyr']):
            valid2 = False
        if not re.fullmatch(r'(1[5-9][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in', p['hgt']):
            valid2 = False
        if not re.fullmatch(r'#([0-9a-f]){6}', p['hcl']):
            valid2 = False
        if not re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', p['ecl']):
            valid2 = False
        if not re.fullmatch(r'\d{9}', p['pid']):
            valid2 = False
        ans2 += valid2

print('Answer 1:', ans1)
print('Answer 2:', ans2)
