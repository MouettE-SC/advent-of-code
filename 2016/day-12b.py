ins = [l.split() for l in [a.strip() for a in open('day-12.input', 'r').readlines()]]

pos = 0
registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

while pos < len(ins):
    i = ins[pos]
    if i[0] == 'cpy':
        if i[1].isdigit():
            registers[i[2]] = int(i[1])
        else:
            registers[i[2]] = registers[i[1]]
        pos += 1
    elif i[0] == 'inc':
        registers[i[1]] += 1
        pos += 1
    elif i[0] == 'dec':
        registers[i[1]] -= 1
        pos += 1
    elif i[0] == 'jnz':
        t = 0
        if i[1].isdigit():
            t = int(i[1])
        else:
            t = registers[i[1]]
        if t != 0:
            pos += int(i[2])
        else:
            pos += 1

print(registers['a'])
