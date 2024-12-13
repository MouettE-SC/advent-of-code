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

    def neighbors(self):
        res2 = []
        if self.r > 0:
            n = nodes[(self.r - 1, self.c)]
            if n.z_id == -1 and n.n == self.n:
                res2.append(n)
        if self.c > 0:
            n = nodes[(self.r, self.c - 1)]
            if n.z_id == -1 and n.n == self.n:
                res2.append(n)
        if self.c < max_c - 1:
            n = nodes[(self.r, self.c + 1)]
            if n.z_id == -1 and n.n == self.n:
                res2.append(n)
        if self.r < max_r - 1:
            n = nodes[(self.r + 1, self.c)]
            if n.z_id == -1 and n.n == self.n:
                res2.append(n)
        return res2

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

c_z_id = 0
while True:
    for (r, c), n in nodes.items():
        if n.z_id != -1:
           continue
        z_id = str(c_z_id)+"|"+n.n
        n.z_id = c_z_id
        p = [n]
        while p:
            cn = p.pop()
            nn = cn.neighbors()
            for n2 in nn:
                n2.z_id = c_z_id
            p.extend(nn)
        c_z_id += 1
        break
    else:
        break

# horizontal sides (by rows)
sides = {}
areas = {}
for z in range(c_z_id):
    sides[z] = 0
    areas[z] = 0
    for r in range(max_r):
        t_broken = True
        b_broken = True
        for c in range(max_c):
            n = nodes[(r, c)]
            if n.z_id == z:
                areas[z] += 1
                if t_broken:
                    if r == 0 or nodes[(r - 1, c)].z_id != z:
                        sides[z] += 1
                        t_broken = False
                elif r > 0 and nodes[(r - 1, c)].z_id == z:
                    t_broken = True
                if b_broken:
                    if r == max_r - 1 or nodes[(r + 1, c)].z_id != z:
                        sides[z] += 1
                        b_broken = False
                elif r < max_r - 1 and nodes[(r + 1, c)].z_id == z:
                    b_broken = True
            else:
                t_broken = True
                b_broken = True

# vertical sides (by columns)
for z in range(c_z_id):
    for c in range(max_c):
        l_broken = True
        r_broken = True
        for r in range(max_r):
            n = nodes[(r, c)]
            if n.z_id == z:
                if l_broken:
                    if c == 0 or nodes[(r, c - 1)].z_id != z:
                        sides[z] += 1
                        l_broken = False
                elif c > 0 and nodes[(r, c - 1)].z_id == z:
                    l_broken = True
                if r_broken:
                    if c == max_c - 1 or nodes[(r, c + 1)].z_id != z:
                        sides[z] += 1
                        r_broken = False
                elif c < max_c - 1 and nodes[(r, c + 1)].z_id == z:
                    r_broken = True
            else:
                l_broken = True
                r_broken = True

ret = 0
for z in range(c_z_id):
    ret += sides[z]*areas[z]
print(ret)