data = ''.join([a.strip() for a in open('day-09.input', 'r').readlines()])

i = 0
r = 0

while i < len(data):
    if data[i] == '(':
        m_end = i+data[i:].find(')')+1
        marker = data[i:m_end]
        m1, m2 = map(int, marker[1:-1].split('x'))
        r += len(data[m_end:m_end + m1] * m2)
        i = m_end + m1
    else:
        r += 1
        i += 1
print(r)



