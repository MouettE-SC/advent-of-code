# see https://www.youtube.com/watch?v=uCsD3ZGzMgE

o = n = int(open('day-19.input', 'r').read())
a = 0

while n != 1:
    a += 1
    n >>= 1

l = o - 2**a
print(2*l + 1)