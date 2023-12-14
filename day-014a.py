rows = []

for l in [a.strip() for a in open('day-014.input', 'r').readlines()]:
    rows.append(l)

rows = [''.join(list(x)) for x in zip(*rows)]

t = 0
for c in rows:
    n_p = len(rows)
    for i, ch in enumerate(c):
        if ch == 'O':
            t += n_p
            n_p -= 1
        elif ch == '#':
            n_p = len(rows) - i - 1

print(t)
