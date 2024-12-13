stones = [int(a) for a in open('day-11.input', 'r').read().split()]

for _ in range(25):
    ns = []
    for s in stones:
        ss = str(s)
        if s == 0:
            ns.append(1)
        elif len(ss) % 2 == 0:
            ns.append(int(ss[0:len(ss) // 2]))
            ns.append(int(ss[len(ss) // 2:]))
        else:
            ns.append(s*2024)
    stones = ns

print(len(stones))