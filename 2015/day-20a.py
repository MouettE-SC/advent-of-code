n = int(open('day-20.input').read())


def div(n):
    if n == 1:
        yield 10
    else:
        for i in range(1, int(n/2)+1):
            if n % i == 0:
                yield i*10
        yield n*10


t = 1
p = sum(div(t))
while p < n:
    t += 1
    p = sum(div(t))

print(t)
