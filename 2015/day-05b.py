t = 0
for l in open('day-05.input', 'r').readlines():
    l = l.strip()
    pl = False
    for i in range(0, len(l)-1):
        p = l[i:i+2]
        if p in l[0:i] or p in l[i+2:]:
            pl = True
            break
    if not pl:
        continue
    rl = False
    for i in range(0, len(l)-2):
        if l[i] == l[i+2]:
            rl = True
            break
    if not rl:
        continue
    t += 1

print(t)
