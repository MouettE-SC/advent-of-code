ins = [(cc[0], int(cc[1:])) for cc in open('day-01.input', 'r').read().split(", ")]

d_map = {'N': {'R': 'E', 'L': 'W'}, 'S': {'R': 'W', 'L': 'E'}, 'E': {'R': 'S', 'L': 'N'}, 'W': {'R': 'N', 'L': 'S'}}

d = 'N'
vh = [0, 0]
seen = [(0, 0)]
for o, n in ins:
    d = d_map[d][o]
    stop = False
    if d == 'N':
        for m in range(1, n+1):
            if (vh[0] + m, vh[1]) in seen:
                stop = True
                r = abs(vh[0] + m) + abs(vh[1])
            else:
                seen.append((vh[0] + m, vh[1]))
        vh[0] += n
    elif d == 'S':
        for m in range(1, n+1):
            if (vh[0] - m, vh[1]) in seen:
                stop = True
                r = abs(vh[0] - m) + abs(vh[1])
            else:
                seen.append((vh[0] - m, vh[1]))
        vh[0] -= n
    elif d == 'E':
        for m in range(1, n+1):
            if (vh[0], vh[1] + m) in seen:
                stop = True
                r = abs(vh[0]) + abs(vh[1] + m)
            else:
                seen.append((vh[0], vh[1] + m))
        vh[1] += n
    elif d == 'W':
        for m in range(1, n+1):
            if (vh[0], vh[1] - m) in seen:
                stop = True
                r = abs(vh[0]) + abs(vh[1] - m)
            else:
                seen.append((vh[0], vh[1] - m))
        vh[1] -= n
    if stop:
        break

print(r)
