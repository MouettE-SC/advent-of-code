rows = []

for l in open('day-014.input', 'r').readlines():
    rows.append([c for c in l.strip()])

print(rows)

def tilt(d: int):
    global rows
    if d in (0, 2):   # N S
        for j in range(len(rows[0])):
            if d == 0:
                c_i = 0
                for i in range(len(rows)):
                    if rows[i][j] == 'O':
                        if i != c_i:
                            rows[c_i][j] = 'O'
                            rows[i][j] = '.'
                        c_i += 1
                    elif rows[i][j] == '#':
                        c_i = i + 1
            elif d == 2:
                c_i = len(rows) - 1
                for i in range(c_i, -1, -1):
                    if rows[i][j] == 'O':
                        if i != c_i:
                            rows[c_i][j] = 'O'
                            rows[i][j] = '.'
                        c_i -= 1
                    elif rows[i][j] == '#':
                        c_i = i-1
    elif d in (1, 3): # W E
        for i in range(len(rows)):
            if d == 1:
                c_j = 0
                for j in range(len(rows[i])):
                    if rows[i][j] == 'O':
                        if j != c_j:
                            rows[i][c_j] = 'O'
                            rows[i][j] = '.'
                        c_j += 1
                    elif rows[i][j] == '#':
                        c_j = j + 1
            elif d == 3:
                c_j = len(rows[i]) - 1
                for j in range(c_j, -1, -1):
                    if rows[i][j] == 'O':
                        if j != c_j:
                            rows[i][c_j] = 'O'
                            rows[i][j] = '.'
                        c_j -= 1
                    elif rows[i][j] == '#':
                        c_j = j - 1


def cycle():
    for d in range(4):
        tilt(d)


def w(lines):
    return sum((len(lines)-i)*l.count('O') for i, l in enumerate(lines))


c = 0
while c < 1000000000:
    p = [[l.copy() for l in rows]]
    cycle()
    c += 1
    while rows not in p:
        p.append([l.copy() for l in rows])
        cycle()
        c += 1
    break

c_start = p.index(rows)
c_end = c
c_length = c_end - c_start

print(w(p[c_start + ((1_000_000_000 - c_start) % c_length)]))


