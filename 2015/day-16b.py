data_eq = {"children": 3, "samoyeds": 2, "akitas": 0, "vizslas": 0, "cars": 2, "perfumes": 1}
data_gt = {"cats": 7, "trees": 3}
data_lt = {"pomeranians": 3, "goldfish": 5}

for l in [a.strip() for a in open('day16.input', 'r').readlines()]:
    cc = l.split(": ", maxsplit=1)
    si = int(cc[0].split()[1])
    cc = cc[1].split(", ")
    sd = {}
    for c in cc:
        s = c.split(": ")
        sd[s[0]] = int(s[1])
    stop = False
    for k, v in data_eq.items():
        if k not in sd:
            continue
        if sd[k] != v:
            stop = True
            break
    if stop:
        continue
    for k, v in data_gt.items():
        if k not in sd:
            continue
        if sd[k] <= v:
            stop = True
            break
    if stop:
        continue
    for k, v in data_lt.items():
        if k not in sd:
            continue
        if sd[k] >= v:
            stop = True
            break
    if stop:
        continue
    print(si)