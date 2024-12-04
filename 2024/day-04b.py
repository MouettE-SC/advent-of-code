data = []
for l in open('day-04.input', 'r').readlines():
    l = l.strip()
    data.append([c for c in l])

ret = 0

for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if data[i][j] != 'A':
            continue
        ul = data[i-1][j-1]
        ur = data[i-1][j+1]
        dl = data[i+1][j-1]
        dr = data[i+1][j+1]
        if (ul, ur, dl, dr) == ('M', 'S', 'M', 'S') or \
            (ul, ur, dl, dr) == ('S', 'S', 'M', 'M') or \
            (ul, ur, dl, dr) == ('M', 'M', 'S', 'S') or \
            (ul, ur, dl, dr) == ('S', 'M', 'S', 'M'):
            ret += 1

print(ret)
