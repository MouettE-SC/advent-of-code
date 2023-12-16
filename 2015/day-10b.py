
def run(l: str):
    r = ""
    last = ''
    n = 0
    for c in l:
        if last == '':
            last = c
            n = 1
        elif last == c:
            n += 1
        else:
            r += str(n) + last
            last = c
            n = 1
    r += str(n) + last
    return r


cl = open('day-10.input', 'r').read()

for _ in range(0, 50):
    cl = run(cl)

print(len(cl))
