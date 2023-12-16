import math

d = ''
m = {}
st = []
for i, l in enumerate([a.strip() for a in open('day-008.input', 'r').readlines()]):
    if i == 0:
        d = l
    elif i >= 2:
        cc = l.split(" = ")
        lr = cc[1][1:-1].split(", ")
        m[cc[0]] = lr
        if cc[0][2] == 'A':
            st.append(cc[0])

costs = []
for s in st:
    di = 0
    i = 0
    p = s
    while True:
        n = d[di]
        p = m[p][0 if n == 'L' else 1]
        i += 1
        if p[2] == 'Z':
            costs.append(i)
            break
        di += 1
        if di == len(d):
            di = 0

print(math.lcm(*costs))


