from itertools import combinations

boss = []
for l in [a.strip() for a in open('day21.input', 'r').readlines()]:
    boss.append(int(l.split()[-1]))


weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]


def play(p1, p2):
    d1 = max(1, p1[1] - p2[2])
    d2 = max(1, p2[1] - p1[2])
    while True:
        p2[0] -= d1
        if p2[0] <= 0:
            return True
        p1[0] -= d2
        if p1[0] <= 0:
            return False


t = 999

for w in range(0, len(weapons)):
    for a in range(-1, len(armor)):
        # no ring case first
        pl = [100, weapons[w][1], armor[a][2] if a != -1 else 0]
        cost = weapons[w][0] + (armor[a][0] if a != -1 else 0)
        if play(pl.copy(), boss.copy()):
            t = min(t, cost)
        for r1, r2 in combinations(range(-1, len(rings)), 2):
            plr = pl.copy()
            cost_r = cost
            if r1 != -1:
                plr[1] += rings[r1][1]
                plr[2] += rings[r1][2]
                cost_r += rings[r1][0]
            if r2 != -1:
                plr[1] += rings[r2][1]
                plr[2] += rings[r2][2]
                cost_r += rings[r2][0]
            if play(plr, boss.copy()):
                t = min(t, cost_r)

print(t)