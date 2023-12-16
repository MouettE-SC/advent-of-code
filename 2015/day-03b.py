c_coord1 = [0, 0]
c_coord2 = [0, 0]
houses = set()
houses.add((0, 0))
i = 0
for c in open('day03.input', 'r').read():
    c_coord = c_coord1 if i % 2 == 0 else c_coord2
    if c == '^':
        c_coord[1] += 1
    elif c == 'v':
        c_coord[1] -= 1
    elif c == '<':
        c_coord[0] -= 1
    elif c == '>':
        c_coord[0] += 1
    houses.add(tuple(c_coord))
    i += 1

print(len(houses))
