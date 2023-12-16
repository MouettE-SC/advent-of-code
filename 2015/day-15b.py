from itertools import product

data = []

for l in [a.strip() for a in open('day-15.input', 'r').readlines()]:
    cc = l.split(": ")
    cc2 = cc[1].split(", ")
    data.append([int(a.split()[1]) for a in cc2])

t = 0
for r in product(range(1, 100), repeat=len(data)):
    if sum(r) != 100:
        continue
    if r[0]*data[0][4] + r[1]*data[1][4] + r[2]*data[2][4] + r[3]*data[3][4] != 500:
        continue
    st = 1
    for i in range(0, 4):
        st *= max(0, r[0]*data[0][i] + r[1]*data[1][i] + r[2]*data[2][i] + r[3]*data[3][i])
    t = max(t, st)
print(t)


