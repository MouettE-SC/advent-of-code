from itertools import chain

grid = []

for l in [a.strip() for a in open('day-16.input', 'r').readlines()]:
    grid.append([c for c in l])

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


def calc(start: tuple[int, int, str]):
    beams = [start]
    c_grid = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]
    seen = []
    while beams:
        i, j, d = beams.pop()
        if (i, j, d) in seen:
            continue
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
            seen.append((i, j, d))
            c_grid[i][j] = True
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
        if nj < 0 or nj >= len(grid[0]):
            continue
        c = grid[ni][nj]
        for nd in d_map[d][c]:
            beams.append((ni, nj, nd))
    return sum(1 for c in chain.from_iterable(c_grid) if c)

r = 0

print('down')
# down
for j in range(len(grid[0])):
    r = max(r, calc((-1, j, 'D')))

print('up')
# up
for j in range(len(grid[-1])):
    r = max(r, calc((len(grid), j, 'U')))

print('right')
# right
for i in range(len(grid)):
    r = max(r, calc((i, -1, 'R')))

print('left')
# left
for i in range(len(grid)):
    r = max(r, calc((i, len(grid[i]), 'L')))

print(r)
