before = dict()
after = dict()

updates = []
for l in open('day-05.input').readlines():
    l = l.strip()
    if not l:
        continue
    if '|' in l:
        cc = [int(a) for a in l.split('|')]
        before.setdefault(cc[1], set()).add(cc[0])
        after.setdefault(cc[0], set()).add(cc[1])
    else:
        updates.append([int(a) for a in l.split(',')])

def check(p):
    for i in range(len(p)):
        v = p[i]
        pb = set(p[0:i])
        pa = set(p[i + 1:])
        if v in after and pb.intersection(after[v]):
            return False, i, True
        if v in before and pa.intersection(before[v]):
            return False, i, False
    return True, -1 , True

def fix(p):
    valid, i, bef = check(p)
    while not valid:
        if bef:
            p = [p[i]] + p[0:i] + p[i+1:]
        else:
            p = p[0:i] + p[i+1:] + [p[i]]
        valid, i, bef = check(p)
    return p

ret = 0
for u in updates:
    c, _, _ = check(u)
    if not c:
        u = fix(u)
        ret += u[int(len(u)/2)]

print(ret)

