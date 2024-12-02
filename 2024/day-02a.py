r = 0
for l in open('day-02.input', 'r').readlines():
    l = l.strip()
    cc = [int(a) for a in l.split()]
    grow = cc[1] > cc[0]
    ok = True
    for i in range(1, len(cc)):
        d = cc[i] - cc[i - 1]
        if d == 0 or abs(d) > 3:
            ok = False
            break
        if grow and d < 0:
            ok = False
            break
        if not grow and d > 0:
            ok = False
            break
    if ok:
        r += 1
print(r)
