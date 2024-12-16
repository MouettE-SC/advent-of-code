from collections import defaultdict
import zlib
import sys

max_r = 103
max_c = 101
rounds = 100
import re

rb = re.compile(r'p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)')

ex_r = max_r // 2
ex_c = max_c // 2

robots = []

class R:

    def __init__(self, r, c, sr, sc):
        self.r = r
        self.c = c
        self.sr = sr
        self.sc = sc

    def step(self):
        pr = self.r + self.sr
        if pr >= 0:
            self.r = pr % max_r
        else:
            self.r = pr - max_r * (pr // max_r)

        pc = self.c + self.sc
        if pc >= 0:
            self.c = pc % max_c
        else:
            self.c = pc - max_c * (pc // max_c)


def grid():
    res = defaultdict(int)
    for r in robots:
        res[(r.r, r.c)] += 1
    return res


for l in [a.strip() for a in open('day-14.input', 'r').readlines()]:
    m = rb.match(l)
    if not m:
        continue
    c, r, vc, vr = map(int, m.groups())
    robots.append(R(r, c, vr, vc))

s = 0
while True:
    s += 1
    print(s, end='\r')
    sys.stdout.flush()
    for r in robots:
        r.step()
    g = grid()
    desc = ""
    for i in range(max_r):
        for j in range(max_c):
            if g[(i, j)] >= 1:
                desc += 'X'
            else:
                desc += '.'
        desc += '\n'

    e = len(zlib.compress(desc.encode()))

    if e < 600:
        print(f"{s}: {e}")
        print(desc)
        break
