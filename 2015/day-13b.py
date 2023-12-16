from itertools import permutations

m = {}
for l in [a.strip() for a in open('day-13.input', 'r').readlines()]:
    cc = l.split()
    n1 = cc[0]
    n2 = cc[-1][0:-1]
    if cc[2] == 'gain':
        sc = int(cc[3])
    else:
        sc = int('-'+cc[3])
    if n1 in m:
        m[n1][n2] = sc
    else:
        m[n1] = {n2: sc}

names = ["Me"] + list(m.keys())

t = 0
for p in permutations(names[1:], len(names) - 1):
    table = [names[0]] + list(p)
    c = 0
    for i in range(0, len(table)):
        if 0 < i < len(table)-1:
            c += m[table[i]][table[i + 1]]
            c += m[table[i + 1]][table[i]]
    t = max(t, c)

print(t)