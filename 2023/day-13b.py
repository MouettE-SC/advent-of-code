def get_cands(line):
    cand = set()
    for j in range(1, len(line)):
        ok = True
        for c1, c2 in zip(line[0:j][::-1], line[j:]):
            if c1 != c2:
                ok = False
                break
        if ok:
            cand.add(j)
    return cand

def p(lines, f):
    raw_cands = {}
    sm_cands = {}
    for i, l in enumerate(lines):
        raw_cands[i] = get_cands(l)
        sm = set()
        for j in range(0, len(l)):
            l2 = l[0:j] + ('#' if l[j] == '.' else '.') + l[j+1:]
            for c in get_cands(l2):
                sm.add(c)
        sm_cands[i] = sm
    orig = raw_cands[0].copy()
    for i in range(1, len(lines)):
        orig &= raw_cands[i]
    for i in range(0, len(lines)):
        r = sm_cands[i]
        for j in range(0, len(lines)):
            if j == i:
                continue
            r &= raw_cands[j]
        r -= orig
        if r:
            break
    if r:
        return list(r)[0]*f
    else:
        return 0


t = 0
cp = []
for l in [a.strip() for a in open('day-13.input').readlines()]:
    if not l:
        r1 = p(cp, 1)
        if r1:
            t += r1
            cp = []
            continue
        else:
            t += p([''.join(list(x)) for x in zip(*cp)], 100)
        cp = []
    else:
        cp.append(l)

t += p(cp, 1)
t += p([''.join(list(x)) for x in zip(*cp)], 100)

print(t)