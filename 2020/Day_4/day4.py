import re

filename = 'input4.txt'
with open(filename) as file:
    data = file.read().split('\n\n')
data = [p.replace('\n', ' ').split() for p in data]

passports = [{f.split(':')[0]: f.split(':')[1] for f in p} for p in data]
req_fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

ans1, ans2 = 0, 0
regex_patterns = {
    'byr': r'19[2-9][0-9]|200[0-2]',
    'iyr': r'20(1[0-9]|20)',
    'eyr': r'20(2[0-9]|30)',
    'hgt': r'(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in',
    'hcl': r'#([0-9a-f]){6}',
    'ecl': r'amb|blu|brn|gry|grn|hzl|oth',
    'pid': r'\d{9}'
}
for p in passports:
    fields = list(p.keys())
    if 'cid' in fields:
        fields.remove('cid')
    valid = sorted(fields) == req_fields
    ans1 += valid
    if valid:
        fields_match = [re.fullmatch(regex_patterns[field], p[field]) is not None for field in fields]
        ans2 += all(fields_match)

print('Answer 1:', ans1)
print('Answer 2:', ans2)
