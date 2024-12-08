grid = []

start = (0, 0)
d = 'u'

for l in open('day-06.input', 'r').readlines():
    l = l.strip()
    if '^' in l:
        start = (len(grid), l.find('^'))
        l = l.replace('^', '.')
    grid.append([a for a in l])

lr = len(grid) - 1
lc = len(grid[0]) - 1

def turn():
    global d
    if d == 'u':
        d = 'r'
    elif d == 'r':
        d = 'd'
    elif d == 'd':
        d = 'l'
    elif d == 'l':
        d = 'u'

def solve():
    global d
    visited = set()
    visited2 = set()
    pos = start
    d = 'u'
    while True:
        if d == 'u':
            if pos[0] == 0:
                break
            np = (pos[0] - 1, pos[1])
        elif d == 'r':
            if pos[1] == lc:
                break
            np = (pos[0], pos[1] + 1)
        elif d == 'd':
            if pos[0] == lr:
                break
            np = (pos[0] + 1, pos[1])
        elif d == 'l':
            if pos[1] == 0:
                break
            np = (pos[0], pos[1] - 1)
        if grid[np[0]][np[1]] == '#':
            turn()
        else:
            visited.add(np)
            if (np[0], np[1], d) in visited2:
                return None, True
            visited2.add((np[0], np[1], d))
            pos = np
    return visited, False

av, _ = solve()

ret = 0

for r, c in av:
    if (r, c) == start:
        continue
    grid[r][c] = '#'
    _, res = solve()
    if res:
        ret += 1
    grid[r][c] = '.'

print(ret)