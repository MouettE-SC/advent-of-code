from collections import OrderedDict
inst = OrderedDict()

for i, l in enumerate(open('day-23.input', 'r').readlines()):
    inst[i] = l.strip().split()

a = 0
b = 0
i = 0

while True:
    if i >= len(inst) or i < 0:
        break
    c = inst[i]
    if c[0] in ('jmp', 'jie', 'jio'):
        if c[0] == 'jmp':
            i += int(c[-1])
        elif c[0] == 'jie':
            if (c[1][0] == 'a' and a % 2 == 0) or (c[1][0] == 'b' and b % 2 == 0):
                i += int(c[-1])
            else:
                i += 1
        elif c[0] == 'jio':
            if (c[1][0] == 'a' and a == 1) or (c[1][0] == 'b' and b == 1):
                i += int(c[-1])
            else:
                i += 1
    else:
        if c[0] == 'hlf':
            if c[1] == 'a':
                a = int(a/2)
            elif c[1] == 'b':
                b = int(b/2)
        elif c[0] == 'tpl':
            if c[1] == 'a':
                a *= 3
            elif c[1] == 'b':
                b *= 3
        elif c[0] == 'inc':
            if c[1] == 'a':
                a += 1
            elif c[1] == 'b':
                b += 1
        i += 1

print(b)
