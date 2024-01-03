sz = 35651584
data = [int(a) for a in open('day-16.input', 'r').read()]
while len(data) < sz:
    b = [1 if c == 0 else 0 for c in data[::-1]]
    data.append(0)
    data += b

data = data[:sz]

while len(data) % 2 == 0:
    nd = []
    for i in range(0, len(data), 2):
        nd.append(1 if data[i] == data[i+1] else 0)
    data = nd

print(''.join(str(c) for c in data))


