# this works on my input but unlikely to be very generalizable

denied = []
for l in [a.strip().split('-') for a in open('day-20.input', 'r').readlines()]:
    denied.append(tuple(map(int, l)))

denied = sorted(denied)

if denied[0][0] != 0:
    print(denied[0][0] - 1)
    exit(0)

for i in range(1, len(denied)):
    if denied[i][0] <= denied[i-1][1]+1:
        continue
    print(denied[i][0] - 1)
    exit(0)

