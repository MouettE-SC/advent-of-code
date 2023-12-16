import hashlib

st = open('day04.input', 'r').read()
i = 1

while not hashlib.md5((st + str(i)).encode()).hexdigest().startswith('000000'):
    i += 1

print(i)