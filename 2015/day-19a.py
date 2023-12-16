import re

l = [a.strip() for a in open('day19.input', 'r').readlines()]

m = l[-1]
conv = {}
for c in l[:-2]:
    cc = c.split(" => ")
    if cc[0] in conv:
        conv[cc[0]].append(cc[1])
    else:
        conv[cc[0]] = [cc[1]]

t = set()

for k, v in conv.items():
    pos = [m.start() for m in re.finditer('(?='+k+')', m)]
    for p in pos:
        for r in v:
            t.add(m[0:p] + r + m[p+len(k):])

print(len(t))