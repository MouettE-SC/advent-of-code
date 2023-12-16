import re

lines = open('day-001.input').readlines()

t = 0

for l in lines:
    l = l.strip()
    s = re.sub('[^0-9]', '', l)
    t += int(s[0] + s[-1])

print(t)
