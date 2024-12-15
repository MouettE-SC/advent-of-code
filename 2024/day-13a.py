import re

from openpyxl.styles.numbers import builtin_format_id

ba_p = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)")
bb_p = re.compile(r"Button B: X\+([0-9]+), Y\+([0-9]+)")
pr_p = re.compile(r"Prize: X=([0-9]+), Y=([0-9]+)")

xa = xb = ya = yb = 0
px = py = 0

ret = 0
for l in [a.strip() for a in open('day-13.input', 'r').readlines()]:
    ma = re.match(ba_p, l)
    if ma:
        xa = int(ma.group(1))
        ya = int(ma.group(2))
        continue
    mb = re.match(bb_p, l)
    if mb:
        xb = int(mb.group(1))
        yb = int(mb.group(2))
        continue
    mp = re.match(pr_p, l)
    if mp:
        px = int(mp.group(1))
        py = int(mp.group(2))
        print(f"xa={xa}, ya={ya}, xb={xb}, yb={yb}, px={px}, py={py}")
        d = xa*yb - xb*ya
        if d == 0:
            raise ValueError("Non résolvable")
        a = (yb*px - xb*py)/d
        b = (xa*py - ya*px)/d
        if a.is_integer() and b.is_integer():
            ret += int(3*a + b)
print(ret)

