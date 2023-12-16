from collections import defaultdict

cc = open('day-15.input', 'r').read().split(',')

def h(s: str):
    r = 0
    for c in s:
        r += ord(c)
        r *= 17
        r = r % 256
    return r


boxes = defaultdict(list)
m_focal = {}

for s in cc:
    if s[-1] == '-':
        l = s[0:-1]
        nb = h(l)
        if l in boxes[nb]:
            boxes[nb].remove(l)
            del m_focal[(nb, l)]
    else:
        ss = s.split('=')
        l = ss[0]
        nb = h(l)
        f = int(ss[1])
        if l not in boxes[nb]:
            boxes[nb].append(l)
        m_focal[(nb, l)] = f

r = 0
for nb in boxes.keys():
    for i, l in enumerate(boxes[nb]):
        r += (nb + 1) * (i+1) * m_focal[nb, l]
print(r)
