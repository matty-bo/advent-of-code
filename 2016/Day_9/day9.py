import re


def decompress_length(s, part=1):
    marker = re.search('\\((.*?)x(.*?)\\)', s)
    if not marker:
        return len(s)
    ms, me = marker.span()[0], marker.span()[1]
    letters, times = int(marker.group(1)), int(marker.group(2))
    common = len(s[:ms]) + decompress_length(s[me+letters:], part)
    if part == 1:
        return common + letters*times
    if part == 2:
        return common + decompress_length(s[me:me + letters], part) * times


with open('input9') as file:
    string = file.read().strip()
ans1 = decompress_length(string)
ans2 = decompress_length(string,2)
print('Answer 1:', ans1)
print('Answer 2:', ans2)
