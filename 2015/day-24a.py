from itertools import combinations
from math import prod

l = tuple(int(a.strip()) for a in open('day-24.input', 'r').readlines())

sz = int(sum(l)/3)


def valid23(p23: tuple[int]) -> bool:
    global sz
    for s23 in range(1, len(p23)):
        for p2 in combinations(p23, s23):
            if sum(p2) == sz:
                return True


best = []
for s1 in range(1, len(l)):
    for p in combinations(l, s1):
        l1 = 1
        while l1 < s1 and sum(p[0:l1]) < sz:
            l1 += 1
        p1 = p[0:l1]
        if sum(p1) != sz:
            continue
        if not valid23(tuple(filter(lambda a: a not in p1, l))):
            break
        if not best or len(best) - 1 > len(p1):
            best = [prod(p1)] + list(p1)
        elif len(best) - 1 == len(p1):
            qe = prod(p1)
            if qe < best[0]:
                best = [qe] + list(p1)
    if best:
        break

print(best[0])
