grid = []
for line in [a.strip() for a in open('day-10.input', 'r').readlines()]:
    grid.append([c for c in line])

st = []
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

count = 1
pos1 = [st, links[st][0]]
pos2 = [st, links[st][1]]

while pos1[1] != pos2[1]:
    m = pos1[1]
    pos1[1] = links[pos1[1]][0] if links[pos1[1]][0] != pos1[0] else links[pos1[1]][1]
    pos1[0] = m
    m = pos2[1]
    pos2[1] = links[pos2[1]][0] if links[pos2[1]][0] != pos2[0] else links[pos2[1]][1]
    pos2[0] = m
    count += 1

print(count)