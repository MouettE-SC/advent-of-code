n = int(open('day-19.input', 'r').read())

a = 0
while 3**a <= n:
    a += 1
a -= 1

l = n - 3**a
if l <= 3**a:
    print(l)
else:
    print(2*l - 3**a)
