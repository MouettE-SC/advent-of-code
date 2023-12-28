ins = [(cc[0], int(cc[1:])) for cc in open('day-01.input', 'r').read().split(", ")]

d_map = {'N': {'R': 'E', 'L': 'W'}, 'S': {'R': 'W', 'L': 'E'}, 'E': {'R': 'S', 'L': 'N'}, 'W': {'R': 'N', 'L': 'S'}}

d = 'N'
vh = [0, 0]
for o, n in ins:
    d = d_map[d][o]
    if d == 'N':
        vh[0] += n
    elif d == 'S':
        vh[0] -= n
    elif d == 'E':
        vh[1] += n
    elif d == 'W':
        vh[1] -= n

print(abs(vh[0]) + abs(vh[1]))
