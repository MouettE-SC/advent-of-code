g = []
for l in [a.strip() for a in open('day18.input', 'r').readlines()]:
    g.append([c for c in l])


def update(st, i, j):
    if i == 0:
        if j == 0:
            n = st[0][1] + st [1][0] + st[1][1]
        elif j == 99:
            n = st[0][98] + st[1][99] + st[1][98]
        else:
            n = st[0][j-1] + st[0][j+1] + st[1][j-1] + st[1][j] + st[1][j+1]
    elif i == 99:
        if j == 0:
            n = st[98][0] + st[98][1] + st[99][1]
        elif j == 99:
            n = st[99][98] + st[98][98] + st[98][99]
        else:
            n = st[99][j-1] + st[99][j+1] + st[98][j-1] + st[98][j] + st[98][j+1]
    else:
        if j == 0:
            n = st[i-1][0] + st[i+1][0] + st[i-1][1] + st[i][1] + st[i+1][1]
        elif j == 99:
            n = st[i-1][99] + st[i+1][99] + st[i-1][98] + st[i][98] + st[i+1][98]
        else:
            n = (st[i-1][j-1] + st[i-1][j] + st[i-1][j+1] +
                 st[i][j-1] + st[i][j+1] +
                 st[i+1][j-1] + st[i+1][j] + st[i+1][j+1])
    if st[i][j] == '#':
        if n.count('#') not in (2, 3):
            return "."
    else:
        if n.count('#') == 3:
            return "#"
    return st[i][j]


for _ in range(0, 100):
    n = [row[:] for row in g]
    for i in range(0, 100):
        for j in range(0, 100):
            n[i][j] = update(g, i, j)
    g = n

print("".join(sum(g, [])).count("#"))
