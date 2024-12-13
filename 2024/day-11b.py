stones = {}
for s in [int(a) for a in open('day-11.input', 'r').read().split()]:
    if s in stones:
        stones[s] += 1
    else:
        stones[s] = 1

def split(n):
    if n == 0:
        return [1]
    else:
        s = str(n)
        if len(s) % 2 == 0:
            return [int(s[0:len(s)//2]), int(s[len(s)//2:])]
        else:
            return [n*2024]

for r in range(75):
    ns = {}
    for n, sz in stones.items():
        for s in split(n):
            if s in ns:
                ns[s] += sz
            else:
                ns[s] = sz
    stones = ns

print(sum(list(stones.values())))