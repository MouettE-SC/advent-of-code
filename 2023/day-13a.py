def p(lines, f):
    # for b in [''.join(pl) for pl in lines]:
    #     print(b)
    # print('-'*20)
    cand = []
    for i, l in enumerate(lines):
        if i == 0:
            for j in range(1, len(l)):
                ok = True
                for c1, c2 in zip(l[0:j][::-1], l[j:]):
                    if c1 != c2:
                        ok = False
                        break
                if ok:
                    cand.append(j)
        else:
            r = []
            for j in cand:
                ok = True
                for c1, c2 in zip(l[0:j][::-1], l[j:]):
                    if c1 != c2:
                        ok = False
                        break
                if not ok:
                    r.append(j)
            for j in r:
                cand.remove(j)
        if len(cand) == 0:
            return 0
    return cand[0]*f

t = 0
cp = []
for l in [a.strip() for a in open('day-013.input').readlines()]:
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