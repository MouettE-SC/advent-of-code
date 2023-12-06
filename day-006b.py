lines = open('day-006.input', 'r').readlines()
time = int("".join(lines[0].split(':')[1].strip().split()))
dist = int("".join(lines[1].split(':')[1].strip().split()))

t = 0
for h in range(0, time):
    d = h * (time - h)
    if d > dist:
        t += 1

print(t)