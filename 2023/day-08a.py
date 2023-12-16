d = ''
m = {}

for i, l in enumerate([a.strip() for a in open('day-08.input', 'r').readlines()]):
    if i == 0:
        d = l
    elif i >= 2:
        cc = l.split(" = ")
        lr = cc[1][1:-1].split(", ")
        m[cc[0]] = lr

i = 0
t = 0
p = 'AAA'
while True:
    n = d[i]
    p = m[p][0 if n == 'L' else 1]
    t += 1
    if p == 'ZZZ':
        break;
    i += 1
    if i == len(d):
        i = 0

print(t)