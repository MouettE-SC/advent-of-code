ins = [l.split() for l in [a.strip() for a in open('day-23.input', 'r').readlines()]]

pos = 0
registers = {
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0
}

def status():
    for i, d in enumerate(zip(ins, registers.items())):
        if i == pos:
            print(f'=> {d[1][0]}: {d[1][1]} {" ".join(d[0])}')
        else:
            print(f'   {d[1][0]}: {d[1][1]} {" ".join(d[0])}')
    i += 1
    while i < len(ins):
        if i == pos:
            print(f'=>      {" ".join(ins[i])}')
        else:
            print(f'        {" ".join(ins[i])}')
        i += 1

while 0 <= pos < len(ins):
    i = ins[pos]
    # status()
    # input()
    if i[0] == 'tgl':
        if i[1] in registers:
            d = pos + registers[i[1]]
        else:
            d = pos + int(i[1])

        if d < 0 or d >= len(ins):
            pos += 1
            continue
        d = ins[d]
        if len(d) == 2:
            if d[0] == 'inc':
                d[0] = 'dec'
            else:
                d[0] = 'inc'
        elif len(d) == 3:
            if d[0] == 'jnz':
                d[0] = 'cpy'
            else:
                d[0] = 'jnz'
        pos += 1
    elif i[0] == 'cpy':
        if i[2] in registers:
            if i[1] in registers:
                registers[i[2]] = registers[i[1]]
            else:
                registers[i[2]] = int(i[1])
        pos += 1
    elif i[0] == 'inc':
        if i[1] in registers:
            registers[i[1]] += 1
        pos += 1
    elif i[0] == 'dec':
        if i[1] in registers:
            registers[i[1]] -= 1
        pos += 1
    elif i[0] == 'jnz':
        t = 0
        if i[1].isdigit():
            t = int(i[1])
        else:
            t = registers[i[1]]
        if t != 0:
            if i[2] in registers:
                pos += registers[i[2]]
            else:
                pos += int(i[2])
        else:
            pos += 1

print(registers['a'])
