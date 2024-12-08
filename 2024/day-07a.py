def check(result, numbers):
    b = {numbers[0], }
    for i in range(1, len(numbers)):
        v = numbers[i]
        if i == len(numbers) - 1:
            for p in b:
                if p + v == result or p * v == result:
                    return True
            return False
        else:
            nb = set()
            for p in b:
                if p + v <= r:
                    nb.add(p + v)
                if p * v <= r:
                    nb.add(p * v)
            if not nb:
                return False
            b = nb

# bruteforce, used for testing
from itertools import product
def check2(result, numbers):
    for op in product('+*', repeat=len(numbers)-1):
        a = numbers[0]
        for i, o in enumerate(op):
            if o == '+':
                a += numbers[i+1]
            else:
                a *= numbers[i+1]
        if a == result:
            return True
    return False

ret = 0
for l in open('day-07.input', 'r').readlines():
    l = l.strip()
    cc = l.split(':')
    r = int(cc[0])
    n = [int(a) for a in cc[1].split()]
    if check(r, n):
        ret += r

print(ret)
