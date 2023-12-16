from operator import itemgetter

t = 0
it = {}
st = ''
for l in [a.strip() for a in open('day09.input', 'r')]:
    cc = l.split()
    if st == '':
        st = cc[0]
    if not cc[0] in it:
        it[cc[0]] = [(cc[2], int(cc[-1]))]
    else:
        it[cc[0]].append((cc[2], int(cc[-1])))
    if not cc[2] in it:
        it[cc[2]] = [(cc[0], int(cc[-1]))]
    else:
        it[cc[2]].append((cc[0], int(cc[-1])))

v = [st]
for i in range(0, len(it)-1):
    n = sorted([c for c in it[st] if c[0] not in v], key=itemgetter(1))[0]
    t += n[1]
    v.append(n[0])
    st = n[0]

print(t)