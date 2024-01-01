import re


def check(p):
    for i in range(len(p) - 3):
        a = p[i:i + 4]
        if a[0] != a[1] and a[0:2] == a[2:4][::-1]:
            return True
    return False


r = 0
for l in [a.strip() for a in open('day-07.input', 'r').readlines()]:
    found = False
    for i, p in enumerate(re.split('\\[|\\]', l)):
        if i % 2 != 0 and check(p):
            found = False
            break
        if not found and check(p):
            found = True
    if found:
        r += 1
print(r)
