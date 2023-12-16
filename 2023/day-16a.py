from itertools import chain

grid = []

for l in [a.strip() for a in open('day-16.input', 'r').readlines()]:
    grid.append([[c, False] for c in l])

d_map = {
    'U': {
        '.': ['U'],
        '/': ['R'],
        '\\': ['L'],
        '|': ['U'],
        '-': ['L', 'R']
    },
    'L': {
        '.': ['L'],
        '/': ['D'],
        '\\': ['U'],
        '|': ['U', 'D'],
        '-': ['L']
    },
    'D': {
        '.': ['D'],
        '/': ['L'],
        '\\': ['R'],
        '|': ['D'],
        '-': ['L', 'R']
    },
    'R': {
        '.': ['R'],
        '/': ['U'],
        '\\': ['D'],
        '|': ['U', 'D'],
        '-': ['R']
    }
}

tb = '\033[94m'
ty = '\033[93m'
tr = '\033[91m'
te = '\033[0m'


def show_grid(raw:bool = False):
    for row in grid:
        l = ''
        for c in row:
            if c[0] == '.':
                if c[1]:
                    l += ty+'#'+te
                else:
                    l += '.'
            elif c[1]:
                l += ty + ('#' if raw else c[0]) + te
            else:
                l += ('.' if raw else c[0])
        print(l)
    print('-'*40)

# show_grid()


beams = [(0, -1, 'R')]
seen = []
while beams:
    i, j, d = beams.pop()
    if (i, j, d) in seen:
        continue
    if j != -1:
        seen.append((i, j, d))
        grid[i][j][1] = True
    ni, nj = i, j
    if d == 'U':
        ni -= 1
    elif d == 'L':
        nj -= 1
    elif d == 'R':
        nj += 1
    elif d == 'D':
        ni += 1
    if ni < 0 or ni >= len(grid):
        continue
    if nj < 0 or nj >= len(grid[i]):
        continue
    nc = grid[ni][nj]
    c = nc[0]
    for nd in d_map[d][c]:
        beams.append((ni, nj, nd))
    # show_grid()

show_grid(False)
print(sum(1 for c in chain.from_iterable(grid) if c[1]))
