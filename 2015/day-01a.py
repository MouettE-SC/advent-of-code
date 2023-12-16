f = 0
for c in open('day01.input', 'r').read():
    if c == '(':
        f += 1
    else:
        f -= 1
print(f)


