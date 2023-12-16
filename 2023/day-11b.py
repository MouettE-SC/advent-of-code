from itertools import combinations

grid = []

for l in [a.strip() for a in open('day-11.input', 'r').readlines()]:
    if l.count('.') == len(l):
        grid.append(['!' for c in l])
    else:
        grid.append([c for c in l])

for j in range(0, len(grid[0])):
    col = "".join([grid[i][j] for i in range(0, len(grid))])
    if col.count('.')+col.count('!') == len(grid):
        for i in range(0, len(grid)):
            grid[i][j] = '!'

g = []
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == '#':
            g.append((i, j))

t = 0
for (i, j), (a, b) in combinations(g, 2):
    d = abs(a-i) + abs(b-j)
    for x in range(min(a, i)+1, max(a, i)):
        if grid[x][0] == '!':
            d += 999999
    for y in range(min(b, j)+1, max(b, j)):
        if grid[0][y] == '!':
            d += 999999
    t += d

print(t)