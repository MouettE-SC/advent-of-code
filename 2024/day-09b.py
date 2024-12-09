
i = 0
disk = []
for c in open('day-09.input', 'r').readline():
    sz = int(c)
    if i % 2 == 0:
        f_id = int(i/2)

    else:
        f_id = -1
    disk.append((f_id, sz))
    i += 1

if disk[-1][0] == -1:
    del disk[-1]

def show():
    for f_id, sz in disk:
        if f_id == -1:
            print('.'*sz, end='')
        else:
            print(str(f_id) * sz, end='')
    print()



c_pos = len(disk) - 1
while True:
    c_id, c_sz = disk[c_pos]
    # print(c_id, ":", end=' ')
    # show()
    if c_id == 1:
        break

    t_pos = 0
    while t_pos < c_pos:
        if disk[t_pos][0] != -1 or disk[t_pos][1] < c_sz:
            t_pos += 1
            continue
        elif disk[t_pos][1] > c_sz:
            disk.insert(t_pos, disk[c_pos])
            disk[t_pos+1] = (-1, disk[t_pos+1][1] - c_sz)
            c_pos += 1
        else:
            disk[t_pos] = disk[c_pos]
        if disk[c_pos - 1][0] == -1:
            disk[c_pos - 1] = (-1, disk[c_pos - 1][1] + c_sz)
            del disk[c_pos]
            c_pos -= 1
        else:
            disk[c_pos] = (-1, c_sz)
        break

    while disk[c_pos][0] != c_id - 1:
        c_pos -= 1

ret = 0
c_pos = 0
for c_id, c_sz in disk:
    if c_id == -1:
        c_pos += c_sz
    else:
        for _ in range(c_sz):
            ret += c_pos * c_id
            c_pos += 1
print(ret)