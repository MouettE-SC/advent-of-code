

grid = []
row = []
for l in [a.strip() for a in open('day-22.input', 'r').readlines()]:
    if not l.startswith('/dev'):
        continue
    cc = l.split()
    cc[0] = tuple(map(lambda a: int(a[1:]), cc[0].split('/')[3].split('-')[1:]))
    if cc[0][1] == 0:
        if row:
            grid.append(row)
        row = []
    used = int(cc[2][:-1])
    if used < 5:
        row.append('_')
        start = cc[0]
    elif used < 100:
        row.append('.')
    else:
        row.append('#')
grid.append(row)

for r in grid:
    print(''.join(r))

# From there, by hand :
#   - 17 up + 22 left + 36 down to reach goal
#   - 1 to bring goal up 1 row
#   - 5*36 to bring it up
# Total : 256
#
# This code solution also works on my input, not really understood how:
# https://www.reddit.com/r/adventofcode/comments/5jor9q/comment/dbhvxwo