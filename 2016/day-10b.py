from collections import defaultdict


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

    def give(self):
        if not self.full():
            raise ValueError(f"bot {self.n} cannot give (not full)")
        if type(self.l_out) is list:
            self.l_out.append(self.low)
        else:
            self.l_out.add(self.low)
        self.low = -1
        if type(self.h_out) is list:
            self.h_out.append(self.high)
        else:
            self.h_out.add(self.high)
        self.high = -1


bots = {}
outputs = defaultdict(list)


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
            lb = outputs[int(cc[6])]
        if cc[-2] == 'bot':
            hb = gb(int(cc[-1]))
        else:
            hb = outputs[int(cc[-1])]
        b.set_out(lb, hb)
    elif cc[0] == 'value':
        b = gb(int(cc[-1]))
        b.add(int(cc[1]))

while any(b.full() for b in bots.values()):
    for b in bots.values():
        if b.full():
            b.give()

print(outputs[0][0] * outputs[1][0] * outputs[2][0])