t = 0

for l in [a.strip() for a in open('day-09.input', 'r').readlines()]:
    rows = []
    cr = [int(a) for a in l.split()]
    rows.append(cr)
    while not all(v == 0 for v in cr):
        nr = [cr[i+1] - cr[i] for i in range(0, len(cr)-1)]
        rows.append(nr)
        cr = nr
    for i, r in reversed(list(enumerate(rows))):
        if i == len(rows) - 1:
            r.append(0)
        else:
            r.append(r[-1] + rows[i+1][-1])
    t += rows[0][-1]

print(t)

