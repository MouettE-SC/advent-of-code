from itertools import combinations

conts = [int(a.strip()) for a in open('day-17.input', 'r').readlines()]

for i in range(1, len(conts)+1):
    t = 0
    for c in combinations(conts, i):
        if sum(c) == 150:
            t += 1
    if t > 0:
        print(t)
        break
