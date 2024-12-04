data = []
for l in open('day-04.input', 'r').readlines():
    l = l.strip()
    data.append([c for c in l])

def find_next(r, c):
    s_pos = []
    if r > 0:
        if c > 0:
            s_pos.append([r - 1, c - 1, 'ul'])
        s_pos.append([r - 1, c, 'u'])
        if c < len(data[0]) - 1:
            s_pos.append([r - 1, c + 1, 'ur'])
    if c > 0:
        s_pos.append([r, c - 1, 'l'])
    if c < len(data[0]) - 1:
        s_pos.append([r, c + 1, 'r'])
    if r < len(data) - 1:
        if c > 0:
            s_pos.append([r + 1, c - 1, 'dl'])
        s_pos.append([r + 1, c, 'd'])
        if c < len(data[0]) - 1:
            s_pos.append([r + 1, c + 1, 'dr'])

    res = []
    for rs in s_pos:
        if data[rs[0]][rs[1]] == 'M':
            res.append(rs)
    return res


ret = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            for ns in find_next(i, j):
                n = 'A'
                while True:
                    if ns[2] == 'ul':
                        np = [ns[0] - 1, ns[1] - 1]
                    elif ns[2] == 'u':
                        np = [ns[0] - 1, ns[1]]
                    elif ns[2] == 'ur':
                        np = [ns[0] - 1, ns[1] + 1]
                    elif ns[2] == 'l':
                        np = [ns[0], ns[1] - 1]
                    elif ns[2] == 'r':
                        np = [ns[0], ns[1] + 1]
                    elif ns[2] == 'dl':
                        np = [ns[0] + 1, ns[1] - 1]
                    elif ns[2] == 'd':
                        np = [ns[0] + 1, ns[1]]
                    elif ns[2] == 'dr':
                        np = [ns[0] + 1, ns[1] + 1]
                    else:
                        break
                    if np[0] < 0 or np[1] < 0 or np[0] >= len(data) or np[1] >= len(data[i]):
                        break
                    elif data[np[0]][np[1]] == n:
                        if n == 'A':
                            n = 'S'
                            ns[0] = np[0]
                            ns[1] = np[1]
                        else:
                            ret += 1
                            break
                    else:
                        break
print(ret)
