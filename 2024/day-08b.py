from itertools import combinations

antennas = dict()
antinodes = set()

r = -1
for l in [a.strip() for a in open('day-08.input', 'r')]:
    r += 1
    c = -1
    for a in l:
        c += 1
        if a != '.':
            antennas.setdefault(a, []).append((r, c))

def check_bounds(i, j):
    global r, c
    return 0 <= i <= r and 0 <= j <= c

for a in antennas.values():
    for a1, a2 in combinations(a, 2):
        antinodes.add(a1)
        antinodes.add(a2)
        ap1 = a1
        ap2 = a2
        while True:
            an1 = (2*ap1[0] - ap2[0], 2*ap1[1] - ap2[1] )
            if check_bounds(an1[0], an1[1]):
                antinodes.add(an1)
                ap2 = ap1
                ap1 = an1
            else:
                break
        ap1 = a1
        ap2 = a2
        while True:
            an2 = (2*ap2[0] - ap1[0], 2*ap2[1] - ap1[1] )
            if check_bounds(an2[0], an2[1]):
                antinodes.add(an2)
                ap1 = ap2
                ap2 = an2
            else:
                break

print(len(antinodes))