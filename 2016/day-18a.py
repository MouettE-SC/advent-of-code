previous = open('day-18.input', 'r').read()
t = previous.count('.')


def status(l, c, r):
    if l == c == r:
        return '.'
    elif (l, c, r) == ('^', '^', '.'):
        return '^'
    elif (l, c, r) == ('.', '^', '^'):
        return '^'
    elif (l, c, r) == ('^', '.', '.'):
        return '^'
    elif (l, c, r) == ('.', '.', '^'):
        return '^'
    else:
        return '.'


for _ in range(39):
    current = ''
    for i in range(len(previous)):
        if i == 0:
            current += status('.', previous[i], previous[i+1])
        elif i == len(previous) - 1:
            current += status(previous[i-1], previous[i], '.')
        else:
            current += status(previous[i-1], previous[i], previous[i + 1])
    t += current.count('.')
    previous = current

print(t)
