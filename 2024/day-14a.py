max_r = 7
max_c = 11

import re

rb = re.compile(r'p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)')

for l in [a.strip() for a in open('day-14.input', 'r').readlines()]:
    m = rb.match(l)
    if not m:
        continue
    r, c, vr, vc = map(int, m.groups())

    pr = r + 100*vr
    if pr >= 0:
        fr = pr % max_r
    else:
        fr = pr - max_r * (pr // max_r)

    pc = c + 100*vc
    if pc >= 0:
        fc = pc % max_c
    else:
        fc = pc - max_c * (pc // max_c)

    print(fr, fc)