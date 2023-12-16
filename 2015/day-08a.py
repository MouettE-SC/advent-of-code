tl = 0
tc = 0
for l in [a.strip() for a in open('day-08.input', 'r').readlines()]:
    skip = 0
    tl += len(l)
    l = l[1:-1]
    for i, c in enumerate(l):
        if skip > 0:
            skip -= 1
        elif c == '\\':
            if l[i+1] == 'x':
                skip = 3
                tc += 1
            else:
                skip = 1
                tc += 1
        else:
            tc += 1

print(tl - tc)
