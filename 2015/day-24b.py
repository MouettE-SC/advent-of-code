from itertools import combinations
from math import prod

l = tuple(int(a.strip()) for a in open('day-24.input', 'r').readlines())

sz = int(sum(l)/4)


def valid34(p34: tuple[int]) -> bool:
    global sz
    for s34 in range(1, len(p34)):
        for p3 in combinations(p34, s34):
            if sum(p3) == sz:
                return True


def valid234(p234: tuple[int]) -> bool:
    global sz
    for s234 in range(1, len(p234)):
        for p2 in combinations(p234, s234):
            if sum(p2) == sz:
                return valid34(tuple(filter(lambda a: a not in p2, p234)))


best = []
for s1 in range(1, len(l)):
    for p in combinations(l, s1):
        l1 = 1
        while l1 < s1 and sum(p[0:l1]) < sz:
            l1 += 1
        p1 = p[0:l1]
        if sum(p1) != sz:
            continue
        if not valid234(tuple(filter(lambda a: a not in p1, l))):
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
