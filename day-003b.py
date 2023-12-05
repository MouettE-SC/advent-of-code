r_lines = open('day-003.input', 'r').readlines()


class C:

    def __init__(self, ch: str):
        self.c = ch
        self.v = False


ls = []
for l in r_lines:
    ls.append([C(c) for c in l.strip()])


def reset():
    for l in ls:
        for c in l:
            c.v = False


t = 0
i = 0
j = 0
ml = len(ls) - 1
mc = 0


def find_numbers():
    loc = []
    if i == 0 and j == 0:
        loc += [(0, 1), (1, 0), (1, 1)]
    elif i == ml and j == mc:
        loc += [(ml, mc - 1), (ml - 1, mc), (ml - 1, mc - 1)]
    elif i == ml and j == 0:
        loc += [(ml, 1), (ml - 1, 1), (ml - 1, 0)]
    elif i == 0 and j == mc:
        loc += [(0, mc - 1), (1, mc - 1), (1, mc)]
    elif i == 0:
        loc += [(0, j - 1), (1, j - 1), (1, j), (1, j + 1), (0, j + 1)]
    elif i == ml:
        loc += [(ml, j - 1), (ml - 1, j - 1), (ml - 1, j), (ml - 1, j + 1), (ml, j + 1)]
    elif j == 0:
        loc += [(i - 1, 0), (i + 1, 0), (i - 1, 1), (i, 1), (i + 1, 1)]
    elif j == mc:
        loc += [(i - 1, mc), (i + 1, mc), (i - 1, mc - 1), (i, mc - 1), (i + 1, mc - 1)]
    else:
        loc += [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    r = []
    reset()
    for a, b in loc:
        if ls[a][b].v or not ls[a][b].c.isdigit():
            continue
        n = ls[a][b].c
        ls[a][b].v = True
        c = b-1
        while c>=0 and ls[a][c].c.isdigit():
            n = ls[a][c].c + n
            ls[a][c].v = True
            c -= 1
        c = b+1
        while c<=mc and ls[a][c].c.isdigit():
            n += ls[a][c].c
            ls[a][c].v = True
            c += 1
        r.append(int(n))
    return r


for i in range(0, ml+1):
    mc = len(ls[i]) - 1
    for j in range(0, mc+1):
        if ls[i][j].c == '*':
            r = find_numbers()
            if len(r) == 2:
                t += r[0]*r[1]

print(t)


