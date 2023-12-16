import re

t = 0
for l in open('day05.input', 'r').readlines():
    l = l.strip()
    nb_vowels = len(re.sub('[^aeiou]', '', l))
    if nb_vowels < 3:
        continue
    c = l[0]
    tr = False
    for i in range(1, len(l)):
        if l[i] == c:
            tr = True
            break
        c = l[i]
    if not tr:
        continue
    if 'ab' in l or 'cd' in l or 'pq' in l or 'xy' in l:
        continue
    t += 1

print(t)
