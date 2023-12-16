t = 0

for l in open('day-02.input', 'r').readlines():
    l = l.strip()
    cc = l.split(':')
    g = int(cc[0].split(' ')[-1])
    mg = 0
    mr = 0
    mb = 0
    for ti in cc[1].split(';'):
        for cd in ti.split(','):
            cd = cd.strip().split(' ')
            if cd[1] == 'green':
                mg = max(mg, int(cd[0]))
            elif cd[1] == 'blue':
                mb = max(mb, int(cd[0]))
            elif cd[1] == 'red':
                mr = max(mr, int(cd[0]))
    t += mg*mr*mb

print(t)