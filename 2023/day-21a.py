grid = []
q = set()

for i, l in enumerate([a.strip() for a in open('day-21.input', 'r').readlines()]):
    r = []
    for j, c in enumerate(l):
        if c in ('.', '#'):
            r.append(c)
        else:
            r.append('.')
            q.add((i, j))
    grid.append(r)

for _ in range(64):
    nq = set()
    for i, j in q:
        if i > 0 and grid[i-1][j] == '.':
            nq.add((i-1, j))
        if i < len(grid)-1 and grid[i+1][j] == '.':
            nq.add((i+1, j))
        if j > 0 and grid[i][j-1] == '.':
            nq.add((i, j-1))
        if j < len(grid[i])-1 and grid[i][j+1] == '.':
            nq.add((i, j+1))
    q = nq

print(len(q))
