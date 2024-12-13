nodes = {}
max_r = 0
max_c = 0

class N:
    def __init__(self, r, c, n):
        self.r = r
        self.c = c
        self.n = n
        self.z_id = -1
        nodes[(r, c)] = self

    def fence(self):
        res1 = 0
        res2 = []
        if self.r > 0:
            n = nodes[(self.r - 1, self.c)]
            if n.n != self.n:
                res1 += 1
            elif n.z_id == -1:
                res2.append(n)
        else:
            res1 += 1
        if self.c > 0:
            n = nodes[(self.r, self.c - 1)]
            if n.n != self.n:
                res1 += 1
            elif n.z_id == -1:
                res2.append(n)
        else:
            res1 += 1
        if self.c < max_c - 1:
            n = nodes[(self.r, self.c + 1)]
            if n.n != self.n:
                res1 += 1
            elif n.z_id == -1:
                res2.append(n)
        else:
            res1 += 1
        if self.r < max_r - 1:
            n = nodes[(self.r + 1, self.c)]
            if n.n != self.n:
                res1 += 1
            elif n.z_id == -1:
                res2.append(n)
        else:
            res1 += 1
        return res1, res2

    def __repr__(self):
        return f"N({self.r}, {self.c}, {self.n}[{self.z_id}])"

r = 0
for l in [a.strip() for a in open('day-12.input', 'r')]:
    c = 0
    for n in l:
        N(r, c, n)
        c += 1
    max_c = max(max_c, c)
    r += 1
max_r = r

areas = {}
fences = {}
ret = 0
c_z_id = 0
while True:
    for (r, c), n in nodes.items():
        if n.z_id != -1:
           continue
        z_id = str(c_z_id)+"|"+n.n
        n.z_id = c_z_id
        areas[z_id] = 0
        fences[z_id] = 0
        p = [n]
        while p:
            cn = p.pop()
            areas[z_id] += 1
            f, nn = cn.fence()
            fences[z_id] += f
            for n2 in nn:
                n2.z_id = c_z_id
            p.extend(nn)
        ret += areas[z_id]*fences[z_id]
        c_z_id += 1
        break
    else:
        break

print(ret)

