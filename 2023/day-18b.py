from collections import defaultdict

v_lines = defaultdict(list)

pos = [0, 0]

for l in [a.strip() for a in open('day-18.input', 'r').readlines()]:
    h = l.split('#')[1][:-1]
    cc = (int(h[0:5], 16), int(h[5]))

    if cc[1] == 0:      # R
        pos[1] += cc[0]
    elif cc[1] == 2:    # L
        pos[1] -= cc[0]
    elif cc[1] == 3:    # U
        v_lines[pos[1]].append([pos[0] - cc[0], pos[0]])
        pos[0] -= cc[0]
    elif cc[1] == 1:    # D
        v_lines[pos[1]].append([pos[0], pos[0] + cc[0]])
        pos[0] += cc[0]

for l in v_lines.values():
    l.sort()

steps = []
for i, (a, b) in enumerate(zip(list(sorted(v_lines.keys())), list(sorted(v_lines.keys()))[1:])):
    steps.append((a, b-1 if i < len(v_lines)-2 else b))

cur_ranges = []
r = 0
cases = set()
for step in steps:
    next_lines = list(sorted([a.copy() for a in v_lines[step[0]]]))
    new_ranges = []
    cur = cur_ranges.pop(0) if cur_ranges else None
    next = next_lines.pop(0) if next_lines else None
    while cur or next:
        if not cur:
            new_ranges.append(next)
            next = next_lines.pop(0) if next_lines else None
        elif not next:
            new_ranges.append(cur)
            cur = cur_ranges.pop(0) if cur_ranges else None
        elif cur == next:              #0
            cases.add('0')
            next = next_lines.pop(0) if next_lines else None
            cur = cur_ranges.pop(0) if cur_ranges else None
        elif cur[1] == next[0]:        #1
            cases.add('1')
            next[0] = cur[0]
            cur = cur_ranges.pop(0) if cur_ranges else None
        elif cur[0] == next[1]:        #2
            cases.add('2')
            cur[0] = next[0]
            next = next_lines.pop(0) if next_lines else None
        elif cur[0] == next[0]:        #7
            if cur[1] < next[1]:       #7a
                cases.add('7a')
                next[0] = cur[1]
                cur = cur_ranges.pop(0) if cur_ranges else None
            elif next[1] < cur[1]:     #7b
                cases.add('7b')
                cur[0] = next[1]
                next = next_lines.pop(0) if next_lines else None
        elif cur[1] == next[1]:        #8
            if cur[0] < next[0]:       #8a
                cases.add('8a')
                new_ranges.append([cur[0], next[0]])
            elif next[0] < cur[0]:     #8b
                cases.add('8b')
                new_ranges.append([next[0], cur[0]])
            cur = cur_ranges.pop(0) if cur_ranges else None
            next = next_lines.pop(0) if next_lines else None
        elif cur[1] < next[0]:         #3
            cases.add('3')
            new_ranges.append(cur)
            cur = cur_ranges.pop(0) if cur_ranges else None
        elif next[1] < cur[0]:         #4
            cases.add('4')
            new_ranges.append(next)
            next = next_lines.pop(0) if next_lines else None
        elif next[0] < cur[1]:         #5
            new_ranges.append([cur[0], next[0]])
            if cur[1] < next[1]:       #5a
                cases.add('5a')
                next[0] = cur[1]
                cur = cur_ranges.pop(0) if cur_ranges else None
            else:                      #5b
                cases.add('5b')
                cur[0] = next[1]
                next = next_lines.pop(0) if next_lines else None
        elif cur[0] < next[1]:         #6
            new_ranges.append([next[0], cur[0]])
            if next[1] < cur[1]:       #6a
                cases.add('6a')
                cur[0] = next[1]
                next = next_lines.pop(0) if next_lines else None
            else:                      #6b
                cases.add('6b')
                next[0] = cur[1]
                cur = cur_ranges.pop(0) if cur_ranges else None
        else:
            raise Exception('Invalid case')
    # print(f"new : {new_ranges}")
    # column step[0]
    c0_new_ranges = [a.copy() for a in new_ranges]
    c0_vlines = [a.copy() for a in v_lines[step[0]]]
    c0_nr = c0_new_ranges.pop(0) if c0_new_ranges else None
    c0_vline = c0_vlines.pop(0) if c0_vlines else None
    c0_r_lines = []
    while c0_nr or c0_vline:
        if not c0_nr:
            while c0_vline:
                if c0_r_lines and c0_vline[0] == c0_r_lines[-1][1]:
                    c0_r_lines[-1][1] = c0_vline[1]
                else:
                    c0_r_lines.append(c0_vline)
                c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif not c0_vline:
            while c0_nr:
                if c0_r_lines and c0_nr[0] == c0_r_lines[-1][1]:
                    c0_r_lines[-1][1] = c0_nr[1]
                else:
                    c0_r_lines.append(c0_nr)
                c0_nr = c0_new_ranges.pop(0) if c0_new_ranges else None
        elif c0_nr == c0_vline:            #0
            c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif c0_nr[0] == c0_vline[0]:      #7
            if c0_nr[1] < c0_vline[1]:     #7a
                raise Exception('Invalid 7a')
            elif c0_vline[1] < c0_nr[1]:   # 7b
                c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif c0_nr[1] == c0_vline[1]:      #8
            if c0_nr[0] < c0_vline[0]:     #8a
                c0_vline = c0_vlines.pop(0) if c0_vlines else None
            elif c0_vline[0] < c0_nr[0]:   #8b
                raise Exception('Invalid 8b')
        elif c0_nr[1] == c0_vline[0]:      #1
            c0_nr[1] = c0_vline[1]
            c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif c0_nr[0] == c0_vline[1]:      #2
            c0_nr[0] = c0_vline[0]
            c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif c0_nr[1] < c0_vline[0]:       #3
            c0_r_lines.append(c0_nr)
            c0_nr = c0_new_ranges.pop(0) if c0_new_ranges else None
        elif c0_vline[1] < c0_nr[0]:       #4
            c0_r_lines.append(c0_vline)
            c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif c0_nr[0] < c0_vline[0]:       #5
            if c0_nr[1] < c0_vline[1]:     #5a
                raise Exception('Invalid 5a')
            elif c0_vline[1] < c0_nr[1]:
                c0_vline = c0_vlines.pop(0) if c0_vlines else None
        elif c0_vline[0] < c0_nr[0]:       #6
            raise Exception('Invalid 6')
        else:
            raise Exception('Invalid')
    c0_merged = []
    for i, l in enumerate(c0_r_lines):
        if i == 0:
            c0_merged.append(l)
        elif c0_merged[-1][1] == l[0]:
            c0_merged[-1][1] = l[1]
        else:
            c0_merged.append(l)
    c0_r = sum(a[1] - a[0] + 1 for a in c0_merged)
    print(f'{step[0]}: {c0_r}')
    r += c0_r

    # columns step[0] + 1 -> step[1]
    c_r = 0
    for a, b in new_ranges:
        c_r += (step[1] - step[0])*(b - a + 1)
    if step[1] != step[0]:
        print(f'{step[0]+1}-{step[1]}: {c_r}')
    r += c_r
    cur_ranges = new_ranges

print(r)