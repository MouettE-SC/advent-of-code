from itertools import combinations

nodes = {}
sz = (0, 0)
for l in [a.strip() for a in open('day-22.input', 'r').readlines()]:
    if not l.startswith('/dev'):
        continue
    cc = l.split()
    cc[0] = tuple(map(lambda a: int(a[1:]), cc[0].split('/')[3].split('-')[1:]))
    sz = (max(sz[0], cc[0][0] + 1), max(sz[1], cc[0][1] + 1))
    nodes[cc[0]] = (int(cc[2][:-1]), int(cc[3][:-1]))

r = 0
for a, b in combinations(nodes.keys(), 2):
    na = nodes[a]
    nb = nodes[b]
    if 0 < na[0] <= nb[1] or 0 < nb[0] <= na[1]:
        print(a, b)
        r += 1
print(r)