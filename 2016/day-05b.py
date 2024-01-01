import string
from hashlib import md5
from random import choice


id = open('day-05.input', 'r').read()

i = 0
pw = [' ' for _ in range(8)]
while len([c for c in pw if c == ' ']) > 0:
    h = md5(f"{id}{i}".encode()).hexdigest()
    if h[:5] == '00000':
        try:
            pos = int(h[5])
            if pos < 8 and pw[pos] == ' ':
                pw[pos] = h[6]
        except ValueError:
            pass
    print(f"\r{i} {''.join([choice(string.digits+string.ascii_lowercase) if pw[i] == ' ' else pw[i] for i in range(8)])}", end='', flush=True)
    i += 1
print(f"\r{i} {''.join(pw)}")
