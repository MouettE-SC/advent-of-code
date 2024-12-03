import re

l = ''.join(open('day-03.input', 'r').readlines()).strip()

r = re.compile('mul\\(([1-9][0-9]*),([1-9][0-9]*)\\)')

res = 0
for m in r.finditer(l):
    res += int(m.group(1))*int(m.group(2))
print(res)