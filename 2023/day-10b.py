grid = []
for line in [a.strip() for a in open('day-10.input', 'r').readlines()]:
    grid.append([c for c in line])

links = {}
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        links[(i, j)] = []


for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        c = grid[i][j]
        u = False
        d = False
        l = False
        r = False
        if c == 'S':
            st = (i, j)
            u, d, l, r = True, True, True, True
        elif c == '|':
            if i == 0:
                d = True
            elif i == len(grid)-1:
                u = True
            else:
                u, d = True, True
        elif c == '-':
            if j == 0:
                r = True
            elif j == len(grid[i])-1:
                l = True
            else:
                r, l = True, True
        elif c == 'L':
            if i == 0:
                if j != len(grid[i])-1:
                    r = True
            elif j == len(grid[i])-1:
                u = True
            else:
                u, r = True, True
        elif c == 'J':
            if i == 0:
                if j != 0:
                    l = True
            elif j == 0:
                u = True
            else:
                l, u = True, True
        elif c == '7':
            if i == len(grid)-1:
                if j != 0:
                    l = True
            elif j == 0:
                d = True
            else:
                d, l = True, True
        elif c == 'F':
            if i == len(grid)-1:
                if j != len(grid[i])-1:
                    r = True
            elif j == len(grid[i])-1:
                d = True
            else:
                r, d = True, True
        if r and grid[i][j+1] in '-J7S':
            links[(i, j)].append((i, j+1))
        if l and grid[i][j-1] in '-LFS':
            links[(i, j)].append((i, j-1))
        if u and grid[i-1][j] in '|7FS':
            links[(i, j)].append((i-1, j))
        if d and grid[i+1][j] in '|LJS':
            links[(i, j)].append((i+1, j))
        j += 1
    i += 1

paths = [st]
pos1 = [st, links[st][0]]
pos2 = [st, links[st][1]]

while pos1[1] != pos2[1]:
    paths += [pos1[1], pos2[1]]
    m = pos1[1]
    pos1[1] = links[pos1[1]][0] if links[pos1[1]][0] != pos1[0] else links[pos1[1]][1]
    pos1[0] = m
    m = pos2[1]
    pos2[1] = links[pos2[1]][0] if links[pos2[1]][0] != pos2[0] else links[pos2[1]][1]
    pos2[0] = m

paths.append(pos1[1])

tb = '\033[94m'
ty = '\033[93m'
tr = '\033[91m'
te = '\033[0m'


class C:

    def __init__(self, c, path, orig):
        self.c = c
        self.path = path
        self.orig = orig
        self.flooded = False

    def show(self):
        if self.flooded:
            return tb + self.c + te
        elif self.path:
            return tr + self.c + te
        elif self.orig:
            return ty + (self.c if self.c != '.' else 'O') + te
        else:
            return self.c # if self.c != '.' else ' '


grid2 = []
for i in range(0, len(grid)):
    r = []
    for j in range(0, len(grid[i])):
        r.append(C(grid[i][j], (i, j) in paths, True))
        if j != len(grid[i])-1:
            r.append(C('.', False, False))
    grid2.append(r)
    if i != len(grid)-1:
        grid2.append([C('.', False, False) for _ in range(0, len(grid[i])*2 - 1)])

for i in range(0, len(grid2)):
    if i % 2 == 0:
        for j in range(1, len(grid2[i]), 2):
            if grid2[i][j-1].c in '-LFS' and grid2[i][j+1].c in '-J7S':
                grid2[i][j].c = '-'
                grid2[i][j].path = grid2[i][j-1].path and grid2[i][j+1].path
    else:
        for j in range(0, len(grid2[i]), 2):
            if grid2[i-1][j].c in '|7FS' and grid2[i+1][j].c in '|LJS':
                grid2[i][j].c = '|'
                grid2[i][j].path = grid2[i-1][j].path and grid2[i+1][j].path

t = 0

def flood(i, j):
    global t
    enclosed = True
    nodes = {(i, j)}
    visited = 0
    while nodes:
        i, j = nodes.pop()
        grid2[i][j].flooded = True
        if grid2[i][j].orig:
            visited += 1
        if i == 0 or i == len(grid2)-1 or j == 0 or j == len(grid2[i])-1:
            enclosed = False
        if i > 0 and not grid2[i-1][j].flooded and not grid2[i-1][j].path:
            nodes.add((i-1, j))
        if i < len(grid2)-1 and not grid2[i+1][j].flooded and not grid2[i+1][j].path:
            nodes.add((i+1, j))
        if j > 0 and not grid2[i][j-1].flooded and not grid2[i][j-1].path:
            nodes.add((i, j-1))
        if j < len(grid2[i]) - 1 and not grid2[i][j+1].flooded and not grid2[i][j+1].path:
            nodes.add((i, j+1))
    if enclosed:
        t += visited


for r in grid2:
    print("".join([c.show() for c in r]))

print("".join(['-' for _ in range(0, len(grid2[0]))]))

for i in range(0, len(grid2)):
    for j in range(0, len(grid2[i])):
        if grid2[i][j].c == '.' and not grid2[i][j].flooded:
            flood(i, j)
            for r in grid2:
                print("".join([c.show() for c in r]))
            print(i, j, t)
            print("".join(['-' for _ in range(0, len(grid2[0]))]))
