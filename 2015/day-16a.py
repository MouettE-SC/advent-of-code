data = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,"akitas": 0,
        "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for l in [a.strip() for a in open('day-16.input', 'r').readlines()]:
    cc = l.split(": ", maxsplit=1)
    si = int(cc[0].split()[1])
    cc = cc[1].split(", ")
    sd = {}
    for c in cc:
        s = c.split(": ")
        sd[s[0]] = int(s[1])
    if sd.items() <= data.items():
        print(si)