screen = [['.' for _ in range(50)] for _ in range(6)]

def rotate(s:list[str], offset:int) -> list[str]:
    res = ['.' for _ in range(len(s))]
    for i in range(len(s)):
        res[(i+offset) % len(s)] = s[i]
    return res


def p_screen():
    for l in screen:
        print(''.join(l).replace('.', ' '))
    print('-' * 50)


for l in [a.strip() for a in open('day-08.input', 'r').readlines()]:
    cc = l.split()
    if cc[0] == 'rect':
        coords = cc[1].split('x')
        nc = int(coords[0])
        nr = int(coords[1])
        for i in range(nr):
            for j in range(nc):
                screen[i][j] = '#'
    elif cc[0] == 'rotate':
        if cc[1] == 'column':
            j = int(cc[2].split('=')[1])
            nc = int(cc[-1])
            c = [screen[i][j] for i in range(len(screen))]
            for i, c in enumerate(rotate(c, nc)):
                screen[i][j] = c
        elif cc[1] == 'row':
            i = int(cc[2].split('=')[1])
            nr = int(cc[-1])
            screen[i] = rotate(screen[i], nr)

p_screen()
