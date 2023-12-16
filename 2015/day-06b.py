from itertools import chain

lights = []
for _ in range(0, 1000):
    lights.append([0 for _ in range(0, 1000)])

for l in open('day06.input', 'r').readlines():
    cc = l.strip().split(',')
    sc = (int(cc[0].split()[-1]), int(cc[1].split()[0]))
    ec = (int(cc[1].split()[-1]), int(cc[2]))
    if l.startswith('turn on'):
        for i in range(sc[0], ec[0]+1):
            for j in range(sc[1], ec[1]+1):
                lights[i][j] += 1
    elif l.startswith('turn off'):
        for i in range(sc[0], ec[0]+1):
            for j in range(sc[1], ec[1]+1):
                lights[i][j] = lights[i][j] - 1 if lights[i][j] >= 1 else 0
    else:
        for i in range(sc[0], ec[0]+1):
            for j in range(sc[1], ec[1]+1):
                lights[i][j] += 2

print(sum(chain.from_iterable(lights)))