from itertools import combinations

conts = [int(a.strip()) for a in open('day17.input', 'r').readlines()]

t = 0
for i in range(1, len(conts)+1):
    for c in combinations(conts, i):
        if sum(c) == 150:
            t += 1

print(t)