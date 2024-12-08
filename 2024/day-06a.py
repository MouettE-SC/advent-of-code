grid = []

pos = (0, 0)
d = 'u'
visited = set()

for l in open('day-06.input', 'r').readlines():
    l = l.strip()
    if '^' in l:
        pos = (len(grid), l.find('^'))
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
    if grid[np[0]][np[1]] == '.':
        visited.add(np)
        pos = np
    else:
        turn()

print(len(visited))