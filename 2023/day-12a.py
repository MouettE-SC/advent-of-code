from itertools import product

def valid(pattern, occurences):
    cc1 = [len(a) for a in pattern.split(".") if a]
    if len(cc1) != len(occurences):
        return False
    for n1, n2 in zip(cc1, occurences):
        if n1 != n2:
            return False
    return True

t = 0
lines = [a.strip() for a in open('day-012.input', 'r').readlines()]
cl = 0
for l in lines:
    cl += 1
    print(f"\r{cl}/{len(lines)}", end='', flush=True)
    cc = l.split()
    c = [int(a.strip()) for a in cc[1].split(",")]
    m = cc[0]
    d = 0
    q = m.count('?')
    for p in product('#.', repeat=q):
        n = m
        for r in p:
            n = n.replace('?', r, 1)
        if valid(n, c):
            d += 1
    print(f" {d}")
    t += d
print()
print(t)