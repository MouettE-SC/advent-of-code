cols = []
i = open('day-06.input', 'r')
for ch in i.readline().strip():
    cols.append([ch])
for l in i.readlines():
    for c, ch in enumerate(l.strip()):
        cols[c].append(ch)

s_cols = [set(cols[i]) for i in range(len(cols))]

r = ''
for i, c in enumerate(cols):
    r += str(min([(ch, cols[i].count(ch)) for ch in s_cols[i]], key=lambda a: a[1])[0])

print(r)
