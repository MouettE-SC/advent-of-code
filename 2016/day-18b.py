previous = open('day-18.input', 'r').read()
t = previous.count('.')


def status(l, r):
    if l != r:
        return '^'
    else:
        return '.'


for _ in range(399_999):
    current = ''
    for i in range(len(previous)):
        if i == 0:
            current += status('.', previous[i+1])
        elif i == len(previous) - 1:
            current += status(previous[i-1], '.')
        else:
            current += status(previous[i-1], previous[i + 1])
    t += current.count('.')
    previous = current

print(t)
