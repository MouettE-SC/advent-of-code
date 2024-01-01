from hashlib import md5

id = open('day-05.input', 'r').read()

i = 0
pw = ''
while len(pw) < 8:
    h = md5(f"{id}{i}".encode()).hexdigest()
    if h[:5] == '00000':
        pw += h[5]
    i += 1
print(pw)
