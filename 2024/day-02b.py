r = 0

def check(levels):
    grow = levels[1] > levels[0]
    ok = True
    for i in range(1, len(levels)):
        d = levels[i] - levels[i - 1]
        if d == 0 or abs(d) > 3:
            ok = False
            break
        if grow and d < 0:
            ok = False
            break
        if not grow and d > 0:
            ok = False
            break
    return ok

for l in open('day-02.input', 'r').readlines():
    l = l.strip()
    cc = [int(a) for a in l.split()]
    if check(cc):
        r += 1
        continue
    for i in range(len(cc)):
        cc2 = cc[:]
        cc2.pop(i)
        if check(cc2):
            r += 1
            break

print(r)
