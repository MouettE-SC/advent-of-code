sz = 272
data = open('day-16.input', 'r').read()

while len(data) < sz:
    data = data + "0" + data[::-1].replace("0", "2").replace("1", "0").replace("2", "1")

data = data[:sz]

while len(data) % 2 == 0:
    nd = ''
    for i in range(0, len(data), 2):
        nd += "1" if data[i] == data[i+1] else "0"
    data = nd

print(data)


