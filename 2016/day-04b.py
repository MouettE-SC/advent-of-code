from collections import defaultdict

for s, h in [a.strip()[0:-1].split('[') for a in open('day-04.input', 'r').readlines()]:
    name = s[0:s.rfind('-')]
    id = int(s[s.rfind('-')+1:])

    letters = []
    for l in set(name):
        if l != '-':
            letters.append([l, name.count(l)])

    rep = defaultdict(str)
    for l, c in letters:
        rep[c] += l
    rh = ''
    for c in sorted(rep.keys(), reverse=True):
        rh += ''.join(sorted(rep[c]))
    if h == rh[0:5]:
        print(name)

