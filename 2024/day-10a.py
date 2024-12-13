nodes = {}
starts = []
max_r = 0
max_c = 0

class N:
    def __init__(self, row, col, height):
        self.r = row
        self.c = col
        self.height = height
        self.seen = False
        nodes[(row, col)] = self
        if self.height == 0:
            starts.append(self)

    def left(self):
        return nodes[(self.r-1, self.c)] if self.r > 0 and nodes[(self.r-1, self.c)].height == self.height + 1 else None

    def right(self):
        return nodes[(self.r+1, self.c)] if self.r < max_r - 1 and nodes[(self.r+1, self.c)].height == self.height + 1 else None

    def top(self):
        return nodes[(self.r, self.c-1)] if self.c > 0 and nodes[(self.r, self.c-1)].height == self.height + 1 else None

    def bottom(self):
        return nodes[(self.r, self.c+1)] if self.c < max_c - 1 and nodes[(self.r, self.c+1)].height == self.height + 1 else None

    def next(self):
        res = []
        l = self.left()
        if l is not None:
            res.append(l)
        r = self.right()
        if r is not None:
            res.append(r)
        t = self.top()
        if t is not None:
            res.append(t)
        b = self.bottom()
        if b is not None:
            res.append(b)
        return res


r = 0
for l in [a.strip() for a in open('day-10.input', 'r').readlines()]:
    c = 0
    for h in l:
        N(r, c, int(h))
        c += 1
    max_c = max(max_c, c)
    r += 1
max_r = r

ret = 0
for s in starts:
    for n in nodes.values():
        n.seen = False
    sc = 0
    next = s.next()
    while next:
        current = next[:]
        next.clear()
        for c in current:
            if c.height == 9:
                if not c.seen:
                    c.seen = True
                    sc += 1
            else:
                next += c.next()
    print(s.r, s.c, sc)
    ret += sc

print(ret)


