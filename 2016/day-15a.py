class Disc:

    def __init__(self, index, sz, pos):
        self.index = index
        self.sz = sz
        self.pos = pos
        self.valid = (-index) % sz

    def is_valid(self):
        return self.pos == self.valid

    def turn(self):
        self.pos = (self.pos + 1) % self.sz

    def __repr__(self):
        return f'#{self.index}: {self.pos}/{self.sz} [{self.valid}]'


discs = []

for cc in [a.strip().split() for a in open('day-15.input', 'r').readlines()]:
    discs.append(Disc(int(cc[1][1:]), int(cc[3]), int(cc[-1][:-1])))

t = 0
while not all(d.is_valid() for d in discs):
    for d in discs:
        d.turn()
    t += 1
    print(f"\r{t}", end='', flush=True)

print()
print(discs)
