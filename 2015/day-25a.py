cc = open('day-25.input', 'r').read().split()

row = int(cc[-3][:-1])
col = int(cc[-1][:-1])

n = row*row + col*col + row*col - sum(range(1, row+2)) - sum(range(1, col+1)) + 2

r = 20151125
for _ in range(n-1):
    r = (r*252533) % 33554393

print(r)
