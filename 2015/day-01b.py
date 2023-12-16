f = 0
i = 1
for c in open('day01.input', 'r').read():
    if c == '(':
        f += 1
    else:
        f -= 1
    if f == -1:
        print(i)
        break
    i += 1


