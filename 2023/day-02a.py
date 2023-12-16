mr = 12
mg = 13
mb = 14

t = 0

for l in open('day-02.input', 'r').readlines():
    l = l.strip()
    cc = l.split(':')
    g = int(cc[0].split(' ')[-1])
    valid = True
    for ti in cc[1].split(';'):
        for cd in ti.split(','):
            cd = cd.strip().split(' ')
            if cd[1] == 'green':
                if int(cd[0]) > mg:
                    valid = False
                    break
            elif cd[1] == 'blue':
                if int(cd[0]) > mb:
                    valid = False
                    break
            elif cd[1] == 'red':
                if int(cd[0]) > mr:
                    valid = False
                    break
        if not valid:
            break
    if valid:
        t += g

print(t)