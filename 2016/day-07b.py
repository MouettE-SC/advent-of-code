import re


def find_abas(p):
    res = set()
    for i in range(len(p) - 2):
        a = p[i:i + 3]
        if a[0] != a[1] and a[0] == a[2]:
            res.add(a)
    return res


r = 0
supernet = []
hypernet = []

for l in [a.strip() for a in open('day-07.input', 'r').readlines()]:
    supernet.clear()
    hypernet.clear()
    for i, p in enumerate(re.split('\\[|\\]', l)):
        if i % 2 != 0:
            hypernet.append(p)
        else:
            supernet.append(p)
    abas = set()
    for p in supernet:
        abas = abas.union(find_abas(p))
    found = False
    for aba in abas:
        if any(p.find(f'{aba[1]}{aba[0]}{aba[1]}') != -1 for p in hypernet):
            found = True
            break
    if found:
        r += 1

print(r)
