r = 0


def valid(a, b, c):
    return a+b > c and a+c > b and b+c > a

t = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

r = 0
i = 0
for a, b, c in [map(int, cc.strip().split()) for cc in open('day-03.input', 'r').readlines()]:
    t[0][i] = a
    t[1][i] = b
    t[2][i] = c
    if i == 2:
        if valid(*t[0]):
            r += 1
        if valid(*t[1]):
            r += 1
        if valid(*t[2]):
            r += 1
        i = 0
    else:
        i += 1

print(r)
