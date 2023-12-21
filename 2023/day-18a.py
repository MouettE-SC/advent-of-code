coords = [(0, 0)]
c = [0, 0]

for l in [a.strip() for a in open('day-18.input', 'r').readlines()]:
    cc = l.split()
    if cc[0] == 'R':
        c[1] += int(cc[1])
    elif cc[0] == 'L':
        c[1] -= int(cc[1])
    elif cc[0] == 'U':
        c[0] -= int(cc[1])
    elif cc[0] == 'D':
        c[0] += int(cc[1])
    coords.append((c[0], c[1]))

r_max = max(coords, key=lambda a: a[0])[0]
r_min = min(coords, key=lambda a: a[0])[0]

c_max = max(coords, key=lambda a: a[1])[1]
c_min = min(coords, key=lambda a: a[1])[1]


grid = [['.' for _ in range(c_min, c_max+1)] for _ in range(r_min, r_max+1)]
for n, (a, b) in enumerate(coords):
    i = a - r_min
    j = b - c_min
    if n > 0:
        pa, pb = coords[n-1]
        pi = pa - r_min
        pj = pb - c_min
        if pi < i:
            for r in range(pi + 1, i):
                grid[r][j] = '#'
        elif i < pi:
            for r in range(i + 1, pi):
                grid[r][j] = '#'
        elif pj < j:
            for c in range(pj + 1, j):
                grid[i][c] = '#'
        elif j < pj:
            for c in range(j+1, pj):
                grid[i][c] = '#'
    grid[i][j] = '#'

res = 0

for i, r in enumerate(grid):
    fill = False
    r = ''.join(r)
    for j, c in enumerate(r):
        if c == '#':
            res += 1
            if i > 0 and grid[i-1][j] == '#':
                fill = not fill
        elif fill:
            res += 1

print(res)
