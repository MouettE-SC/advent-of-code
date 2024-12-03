import re

l = ''.join(open('day-03.input', 'r').readlines()).strip()

r = re.compile('(mul\\(([1-9][0-9]*),([1-9][0-9]*)\\)|do\\(\\)|don\'t\\(\\))')

res = 0
enabled = True
for m in r.finditer(l):
    if m.group(1) == 'do()':
        enabled = True
    elif m.group(1) == 'don\'t()':
        enabled = False
    elif enabled:
        res += int(m.group(2))*int(m.group(3))
print(res)