from itertools import combinations
from collections import deque

types = ''


class State:

    def __init__(self):
        self.elevator = 1
        self.floors = [(set(), set()), (set(), set()), (set(), set()), (set(), set())]

    def print(self):
        r = ''
        for i in range(4, 0, -1):
            r += f'F{i} '
            r += 'E ' if self.elevator == i else '. '
            for t in types:
                r += f'{t}G ' if t in self.floors[i-1][0] else '.  '
                r += f'{t}M ' if t in self.floors[i-1][1] else '.  '
            if i != 1:
                r += '\n'
        print(r)

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        if self.elevator != other.elevator:
            return False
        t_map = {t: '' for t in types}
        for f in range(len(self.floors)):
            if len(self.floors[f][0]) != len(other.floors[f][0]) or len(self.floors[f][1]) != len(other.floors[f][1]):
                return False
            for g1, g2 in zip(sorted(self.floors[f][0]), sorted(other.floors[f][0])):
                if not t_map[g1]:
                    t_map[g1] = g2
                elif g2 != t_map[g1]:
                    return False
        return True

    def __repr__(self):
        r = f'E{self.elevator}'
        for f in range(1, 5):
            r += f' {f}['
            elts = []
            for t in types:
                if t in self.floors[f - 1][0]:
                    elts.append(f'{t}G')
                if t in self.floors[f - 1][1]:
                    elts.append(f'{t}M')
            r += ','.join(elts)
            r += ']'
        return r

    def allowed_moves(self):
        f = self.elevator
        gs = self.floors[f-1][0]
        ms = self.floors[f-1][1]
        moves = []
        for g in gs:
            moves.append(({g}, set()))
        for g in combinations(gs, 2):
            moves.append((set(g), set()))
        for m in ms:
            moves.append((set(), {m}))
        for m in combinations(ms, 2):
            moves.append((set(), set(m)))
        for g in gs:
            for m in ms:
                moves.append((set(g), set(m)))
        if f == 1:
            av_floors = [2]
        elif f == 4:
            av_floors = [3]
        else:
            av_floors = [f-1, f+1]

        res = []
        for nf in av_floors:
            for ngs, nms in moves:
                nst = self.move(f, nf, ngs, nms)
                if nst.valid():
                    res.append(nst)
        return res

    def valid(self) -> bool:
        return all(not ms - gs or not gs for gs, ms in self.floors)

    def move(self, of, nf, ngs, nms):
        res = State()
        res.elevator = nf
        for i in range(1, 5):
            if i == of:
                res.floors[i-1] = (self.floors[i-1][0] - ngs, self.floors[i-1][1] - nms)
            elif i == nf:
                res.floors[i-1] = (self.floors[i-1][0].union(ngs), self.floors[i-1][1].union(nms))
            else:
                res.floors[i-1] = (self.floors[i-1][0].copy(), self.floors[i-1][1].copy())
        return res


initial_state = State()
for l in [a.strip() for a in open('day-11.input', 'r').readlines()]:
    cc = l.split()
    if cc[1] == 'first':
        fl = initial_state.floors[0]
    elif cc[1] == 'second':
        fl = initial_state.floors[1]
    elif cc[1] == 'third':
        fl = initial_state.floors[2]
    elif cc[1] == 'fourth':
        fl = initial_state.floors[3]
    for i in range(len(cc)):
        if cc[i] in ('microchip', 'microchip,', 'microchip.', 'generator,', 'generator', 'generator.'):
            t = cc[i-1][0].upper()
            if t not in types:
                types += t
            if cc[i][0] == 'm':
                fl[1].add(t)
            else:
                fl[0].add(t)

types = ''.join(sorted(types))

final_state = State()
final_state.elevator = 4
final_state.floors[3] = (set(types), set(types))


seen = [initial_state]
q = deque([(0, initial_state)])
while q:
    n, state = q.popleft()
    for m in state.allowed_moves():
        if m == final_state:
            print(n+1)
            exit(0)
        elif not m in seen:
            seen.append(m)
            q.append((n+1, m))
