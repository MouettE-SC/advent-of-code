r_lines = open('day-03.input', 'r').readlines()
lines = []
for l in r_lines:
    lines.append([c for c in l.strip()])


def is_valid(ch: str):
    return not ch.isdigit() and ch != '.'

def v_all(i, j):
    return v_left(i, j) | v_center(i, j) | v_right(i, j)

def v_left(i, j):
    r = v_center(i, j)
    if j == 0:
        return r
    if i == 0:
        return r or is_valid(lines[i][j-1]) or is_valid(lines[i+1][j-1])
    elif i == len(lines) - 1:
        return r or is_valid(lines[i][j-1]) or is_valid(lines[i-1][j-1])
    else:
        return r or is_valid(lines[i][j-1]) or is_valid(lines[i+1][j-1]) or is_valid(lines[i-1][j-1])

def v_right(i, j):
    r = v_center(i, j)
    if j == len(lines[i])-1:
        return r
    if i == 0:
        return r or is_valid(lines[i][j+1]) or is_valid(lines[i+1][j+1])
    elif i == len(lines) - 1:
        return r or is_valid(lines[i][j+1]) or is_valid(lines[i-1][j+1])
    else:
        return r or is_valid(lines[i][j+1]) or is_valid(lines[i-1][j+1]) or is_valid(lines[i+1][j+1])

def v_center(i, j):
    r = False
    if i == 0:
        return is_valid(lines[i+1][j])
    elif i == len(lines) - 1:
        return is_valid(lines[i-1][j])
    else:
        return is_valid(lines[i-1][j]) or is_valid(lines[i+1][j])


t = 0
c = ''
v = False
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j].isdigit():
            v |= v_all(i, j)
            c += lines[i][j]
            if j == len(lines[i]) - 1:
                if v:
                    t += int(c)
                c = ''
                v = False
        elif c:
            if v:
                t += int(c)
            c = ''
            v = False

print(t)
