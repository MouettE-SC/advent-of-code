r = 0

for a, b, c in [map(int, cc.strip().split()) for cc in open('day-03.input', 'r').readlines()]:
    if a+b > c and a+c > b and b+c > a:
        r += 1

print(r)
