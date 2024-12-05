before = dict()
after = dict()

updates = []
for l in open('day-05.input').readlines():
    l = l.strip()
    if not l:
        continue
    if '|' in l:
        cc = [int(a) for a in l.split('|')]
        before.setdefault(cc[1], set()).add(cc[0])
        after.setdefault(cc[0], set()).add(cc[1])
    else:
        updates.append([int(a) for a in l.split(',')])

ret = 0
for u in updates:
    valid = True
    for i in range(len(u)):
        v = u[i]
        pb = set(u[0:i])
        pa = set(u[i+1:])
        if v in after and pb.intersection(after[v]):
            valid = False
            break
        if v in before and pa.intersection(before[v]):
            valid = False
            break
    if valid:
        ret += u[int(len(u)/2)]

print(ret)

