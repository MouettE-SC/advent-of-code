# Painfully slow but works nonetheless

from collections import deque

o_data = ''.join([a.strip() for a in open('day-09.input', 'r').readlines()])


def decode_marker_at(i):
    m_end = i + o_data[i:].find(')') + 1
    marker = o_data[i:m_end]
    m1, m2 = map(int, marker[1:-1].split('x'))
    return m_end, m1, m2


def get_marger_length(m):
    return 3 + len(str(m[0])) + len(str(m[1]))


i = 0
data = deque()
c = 0
while i < len(o_data):
    if o_data[i] == '(':
        if c > 0:
            data.append(c)
            c = 0
        m_end, m1, m2 = decode_marker_at(i)
        data.append((m1, m2))
        i = m_end
    else:
        c += 1
        i += 1
if c > 0:
    data.append(c)

r = 0
while any(type(a) is tuple for a in data):
    n = data.popleft()
    if type(n) is int:
        r += n
    else:
        elts = []
        t = n[0]
        while t > 0:
            m = data.popleft()
            if type(m) is int:
                if m <= t:
                    elts.append(m)
                    t -= m
                else:
                    elts.append(t)
                    data.appendleft(m-t)
                    t = 0
            else:
                sm = get_marger_length(m)
                if sm > t:
                    print("Cannot break marker !")
                    exit(1)
                elts.append(m)
                t -= sm
        data.extendleft(elts[::-1]*n[1])

r += sum(data)
print(r)




