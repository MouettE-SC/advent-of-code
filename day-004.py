import functools


class C:

    def __init__(self, w: int):
        self.n = 1
        self.w = w


cards = []

for l in open('day-004.input', 'r').readlines():
    cc = l.strip().split(':')
    cc = cc[1].split('|')
    w = [int(c.strip()) for c in cc[0].strip().split()]
    m = [int(c.strip()) for c in cc[1].strip().split()]
    nw = 0
    for n in m:
        if n in w:
            nw += 1
    cards.append(C(nw))

for i in range(0, len(cards)):
    c = cards[i]
    for _ in range(1, c.n + 1):
        p = i + 1
        while p < len(cards) and p - i <= c.w:
            cards[p].n += 1
            p += 1

print(functools.reduce(lambda t, i: t + i.n, cards, 0))
