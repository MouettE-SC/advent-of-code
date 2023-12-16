c_coord = [0, 0]
houses = set()
houses.add((0, 0))

for c in open('day-03.input', 'r').read():
    if c == '^':
        c_coord[1] += 1
    elif c == 'v':
        c_coord[1] -= 1
    elif c == '<':
        c_coord[0] -= 1
    elif c == '>':
        c_coord[0] += 1
    houses.add(tuple(c_coord))

print(len(houses))
