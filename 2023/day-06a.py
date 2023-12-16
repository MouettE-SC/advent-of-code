lines = open('day-06.input', 'r').readlines()
times = [int(t) for t in lines[0].split(':')[1].strip().split()]
dists = [int(d) for d in lines[1].split(':')[1].strip().split()]
print(times)
print(dists)

t = 1
for i in range(0, len(times)):
    w = 0
    for h in range(0, times[i]):
        d = h * (times[i] - h)
        if d > dists[i]:
            w += 1
    t *= w

print(t)