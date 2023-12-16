t = 0
for l in open('day-02.input', 'r').readlines():
    l = l.strip()
    sz = [int(a) for a in l.split("x")]
    sz = [sz[0]*sz[1], sz[1]*sz[2], sz[0]*sz[2]]
    t += 2*sz[0] + 2*sz[1] + 2*sz[2] + min(sz)

print(t)