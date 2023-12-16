from itertools import combinations

grid = []

for l in [a.strip() for a in open('day-11.input', 'r').readlines()]:
    grid.append([c for c in l])
    if l.count('.') == len(l):
        grid.append([c for c in l])

ca = []
for j in range(0, len(grid[0])):
    col = "".join([grid[i][j] for i in range(0, len(grid))])
    if col.count('.') == len(grid):
        ca.append(j)

for j in reversed(ca):
    for i in range(0, len(grid)):
        grid[i].insert(j, '.')

g = []
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == '#':
            g.append((i, j))

t = 0
for (i, j), (a, b) in combinations(g, 2):
    t += abs(i-a) + abs(j-b)

print(t)