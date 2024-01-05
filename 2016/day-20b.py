denied = []
for l in [a.strip().split('-') for a in open('day-20.input', 'r').readlines()]:
    denied.append(tuple(map(int, l)))

denied = sorted(denied)

r = 0
up = 0
for a, b in denied:
    if a > up:
        r += a - up - 1
    up = max(up, b)
print(r)

