l1 = []
l2 = []
for l in open('day-01.input', 'r').readlines():
    l = l.strip()
    cc = [int(a) for a in l.split()]
    l1.append(cc[0])
    l2.append(cc[1])
l1.sort()
l2.sort()
r = 0
for i in range(len(l1)):
    r += abs(l1[i] - l2[i])
print(r)