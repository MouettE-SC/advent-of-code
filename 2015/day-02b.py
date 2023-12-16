t = 0
for l in open('day-02.input', 'r').readlines():
    l = l.strip()
    sz1 = [int(a) for a in l.split("x")]
    sz2 = [a for a in sz1 if a != max(sz1)]
    if len(sz2) == 0:
        sz2 = [sz1[0], sz1[1]]
    elif len(sz2) == 1:
        sz2.append(max(sz1))
    t += 2*(sz2[0]+sz2[1]) + sz1[0]*sz1[1]*sz1[2]

print(t)