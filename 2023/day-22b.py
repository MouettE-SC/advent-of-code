from collections import defaultdict, deque

class Brick:
    
    def __init__(self, sx, sy, sz, ex, ey, ez):
        if sz <= ez:
            self.sx = sx
            self.sy = sy
            self.sz = sz
            self.ex = ex
            self.ey = ey
            self.ez = ez
        else:
            self.sx = ex
            self.sy = ey
            self.sz = ez
            self.ex = sx
            self.ey = sy
            self.ez = sz

    def __repr__(self):
        return str((self.sx, self.sy, self.sz, self.ex, self.ey, self.ez))

    def overlaps(self, other):
        return max(self.sx, other.sx) <= min(self.ex, other.ex) and max(self.sy, other.sy) <= min(self.ey, other.ey)


bricks = []
for i, l in enumerate([a.strip() for a in open('day-22.input', 'r').readlines()]):
    cc = l.split('~')
    cc1 = tuple(map(int, cc[0].split(',')))
    cc2 = tuple(map(int, cc[1].split(',')))
    bricks.append(Brick(*cc1, *cc2))

bricks.sort(key=lambda b: b.sz)

# simulate fall

for i, up in enumerate(bricks):
    if up.sz == 1:
        continue
    min_z = 1
    for below in bricks[:i]:
        if below.overlaps(up):
            min_z = max(min_z, below.ez + 1)
    up.ez = min_z + (up.ez - up.sz)
    up.sz = min_z

bricks.sort(key=lambda b: b.sz)

k_supports_v = defaultdict(set)
k_is_supported_by_v = defaultdict(set)

for i, up in enumerate(bricks):
    for j, below in enumerate(bricks[:i]):
        if up.sz == below.ez + 1 and below.overlaps(up):
            k_supports_v[j].add(i)
            k_is_supported_by_v[i].add(j)


r = 0
for i in range(len(bricks)):
    q = deque(j for j in k_supports_v[i] if len(k_is_supported_by_v[j]) == 1)
    fall = set(q)
    fall.add(i)
    while q:
        j = q.popleft()
        for k in k_supports_v[j] - fall:
            if k_is_supported_by_v[k] <= fall:
                q.append(k)
                fall.add(k)

    r += len(fall) - 1
print(r)



