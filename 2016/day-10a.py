class Bot:

    def __init__(self, n):
        self.n = n
        self.low = -1
        self.high = -1
        self.l_out = None
        self.h_out = None

    def full(self):
        return self.low >=0 and self.high >= 0

    def __repr__(self):
        return str(self.n)

    def set_out(self, l_out, h_out):
        self.l_out = l_out
        self.h_out = h_out

    def add(self, v):
        if self.full():
            raise ValueError(f"bot {self.n} already full")
        if self.low == -1:
            self.low = v
        elif self.low > v:
            self.high = self.low
            self.low = v
        else:
            self.high = v
        if self.low == 17 and self.high == 61:
            print(self.n)
            exit(0)

    def give(self):
        if not self.full():
            raise ValueError(f"bot {self.n} cannot give (not full)")
        if self.l_out:
            self.l_out.add(self.low)
        self.low = -1
        if self.h_out:
            self.h_out.add(self.high)
        self.high = -1


bots = {}


def gb(b_id):
    global bots
    if b_id not in bots:
        b = Bot(b_id)
        bots[b_id] = b
    else:
        b = bots[b_id]
    return b


for l in [a.strip() for a in open('day-10.input', 'r').readlines()]:
    cc = l.split()
    if cc[0] == 'bot':
        b = gb(int(cc[1]))
        if cc[5] == 'bot':
            lb = gb(int(cc[6]))
        else:
            lb = None
        if cc[-2] == 'bot':
            hb = gb(int(cc[-1]))
        else:
            hb = None
        b.set_out(lb, hb)
    elif cc[0] == 'value':
        b = gb(int(cc[-1]))
        b.add(int(cc[1]))

while any(b.full() for b in bots.values()):
    for b in bots.values():
        if b.full():
            b.give()

