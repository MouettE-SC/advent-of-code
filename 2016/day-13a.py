from collections import deque

grid = {}

fav = int(open('day-13.input', 'r').read())

dest = (31, 39)

start = (1, 1)
grid[start] = False
grid[dest] = True

q = deque([(0, start)])


def allowed(i, j):
    if i < 0 or j < 0:
        return False
    if (i, j) in grid:
        return grid[(i, j)]
    res = (i*i + 3*i + 2*i*j + j + j*j + fav).bit_count() % 2 == 0
    grid[(i, j)] = res
    return res


while q:
    n, (i, j) = q.popleft()
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if (ni, nj) == dest:
            print(n+1)
            exit(0)
        if allowed(ni, nj):
            grid[(ni, nj)] = False
            q.append((n+1, (ni, nj)))