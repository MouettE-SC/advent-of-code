cc = open('day-015.input', 'r').read().split(',')


def h(s: str):
    r = 0
    for c in s:
        r += ord(c)
        r *= 17
        r = r % 256
    return r


print(sum(h(s) for s in cc))
