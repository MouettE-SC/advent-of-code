# method taken from https://www.youtube.com/watch?v=NTLYL7Mg2jU

grid = []
for l in [a.strip() for a in open('day-23.input', 'r').readlines()]:
    grid.append(l)

start = (0, grid[0].find('.'))
end = (len(grid)-1, grid[-1].find('.'))

points = [start]

for i, l in enumerate(grid):
    for j, c in enumerate(l):
        if grid[i][j] == '#':
            continue
        count = 0
        for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] != '#':
                count += 1
        if count > 2:
            points.append((i, j))

points.append(end)

# graph points
graph = {k: set() for k in points if k != end}
for si, sj in points:
    if (si, sj) == end:
        continue
    q = [(0, si, sj)]
    seen = [(si, sj)]
    while q:
        d, i, j = q.pop()
        if d != 0 and (i, j) in points:
            graph[(si, sj)].add((d, i, j))
            continue
        seen.append((i, j))
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and (ni, nj) not in seen and grid[ni][nj] != '#':
                q.append((d+1, ni, nj))


seen = []

def find_longest(point):
    if point == end:
        return 0

    d = -float("inf")
    seen.append(point)
    for nd, ni, nj in graph[point]:
        if (ni, nj) in seen:
            continue
        d = max(d, find_longest((ni, nj)) + nd)
    seen.remove(point)
    return d

print(find_longest(start))
