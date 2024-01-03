from collections import deque
from hashlib import md5

passcode = open('day-17.input', 'r').read()


def next_steps(i, j, path):
    res = []
    for n, c in enumerate(md5(f'{passcode}{path}'.encode()).hexdigest()[0:4]):
        if ord(c) >= 98:  # b, c, d, e
            if n == 0:
                if i > 0:
                    res.append((i-1, j, f'{path}U'))
            elif n == 1:
                if i < 3:
                    res.append((i+1, j, f'{path}D'))
            elif n == 2:
                if j > 0:
                    res.append((i, j-1, f'{path}L'))
            elif n == 3:
                if j < 3:
                    res.append((i, j+1, f'{path}R'))
    return res

dest = (3, 3)

q = deque([(0, 0, '')])

while q:
    i, j, path = q.popleft()
    for ni, nj, npath in next_steps(i, j, path):
        if (ni, nj) == dest:
            print(npath)
            exit(0)
        q.append((ni, nj, npath))