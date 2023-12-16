tl = 0
te = 0
for l in [a.strip() for a in open('day08.input', 'r').readlines()]:
    skip = 0
    tl += len(l)
    te += 2
    for c in l:
        if c in ('"', '\\'):
            te += 2
        else:
            te += 1

print(te - tl)
