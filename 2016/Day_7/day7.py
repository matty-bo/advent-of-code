import re


def tls(ip):
    res = False
    for string in re.split('\[.*?\]', ip):
        if re.search('(.)(?!\\1)(.)(\\2)(\\1)', string):
            res = True
    if re.search('\[[^\]]*?(.)(?!\\1)(.)(\\2)(\\1).*?\]', ip):
        res = False
    return res

def ssl(ip):
    brackets = re.findall('\[(.*?)\]', ip)
    out = re.split('\[.*?\]', ip)
    out_seq = [seq[1]+seq[0]+seq[1] for s in out for seq in re.findall('(?=(.)(.)(\\1))', s)]
    brackets_seq = [''.join(seq) for s in brackets for seq in re.findall('(?=(.)(.)(\\1))', s)]
    for s in out_seq:
        if s in brackets_seq:
            return True
    return False


with open('input7.txt') as file:
    data = [ip.strip() for ip in file]
ans1, ans2 = 0, 0
for ip in data:
    ans1 += tls(ip)
    ans2 += ssl(ip)
print('Answer 1:', ans1)
print('Answer 2:', ans2)

