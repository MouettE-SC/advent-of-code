def valid(pw: str):
    step1 = False
    for i in range(0, len(pw)-2):
        if pw[i+1] == chr(ord(pw[i])+1) and pw[i+2] == chr(ord(pw[i])+2):
            step1 = True
            break
    if not step1:
        return False
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    i = 0
    dc = 0
    step3 = False
    while i < len(pw) - 1:
        if pw[i] == pw[i+1]:
            dc += 1
            if dc == 2:
                step3 = True
                break
            i += 2
        else:
            i += 1
    return step3


def inc(pw):
    v = [ord(c) for c in pw]
    for i in range(len(v)-1, -1, -1):
        if v[i] == 122:
            v[i] = 97
        else:
            v[i] += 1
            break
    return "".join([chr(c) for c in v])


p = open('day-11.input', 'r').read()
p = inc(p)

while not valid(p):
    p = inc(p)

print(p)