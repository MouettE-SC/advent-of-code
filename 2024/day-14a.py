from functools import reduce

max_r = 103
max_c = 101
rounds = 100
import re
from collections import defaultdict

rb = re.compile(r'p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)')

ex_r = max_r // 2
ex_c = max_c // 2

robots = defaultdict(int)

for l in [a.strip() for a in open('day-14.input', 'r').readlines()]:
    m = rb.match(l)
    if not m:
        continue
    c, r, vc, vr = map(int, m.groups())

    pr = r + rounds*vr
    if pr >= 0:
        fr = pr % max_r
    else:
        fr = pr - max_r * (pr // max_r)

    pc = c + rounds*vc
    if pc >= 0:
        fc = pc % max_c
    else:
        fc = pc - max_c * (pc // max_c)

    robots[(fr, fc)] += 1


quads = {'tl': 0, 'tr': 0, 'bl': 0, 'br': 0}
for i in range(max_r):
    for j in range(max_c):
        r = robots[(i,j)]
        if i < ex_r and j < ex_c:
            quads['tl'] += r
        elif i < ex_r and j > ex_c:
            quads['tr'] += r
        elif i > ex_r and j < ex_c:
            quads['bl'] += r
        elif i > ex_r and j > ex_c:
            quads['br'] += r

print(reduce(lambda x, y: x * y, quads.values()))
