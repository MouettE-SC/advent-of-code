class C:

    def __init__(self, l):
        cc = [a.strip() for a in l.split("->")]
        self.o = cc[1]
        cc = cc[0].split()
        if len(cc) == 1:
            self.op = None
            self.i = [cc[0]]
        elif len(cc) == 2:
            self.op = 'NOT'
            self.i = [cc[1]]
        elif len(cc) == 3:
            self.op = cc[1]
            self.i = [cc[0], cc[2]]

    def run(self, vars: dict):
        if self.op is None:
            if self.i[0].isdigit():
                return int(self.i[0])
            else:
                return vars[self.i[0]]
        elif self.op == 'NOT':
            if self.i[0].isdigit():
                return ~ int(self.i[0])
            else:
                return ~ vars[self.i[0]]
        elif self.op == 'AND':
            l = int(self.i[0]) if self.i[0].isdigit() else vars[self.i[0]]
            r = int(self.i[1]) if self.i[1].isdigit() else vars[self.i[1]]
            return l & r
        elif self.op == 'OR':
            l = int(self.i[0]) if self.i[0].isdigit() else vars[self.i[0]]
            r = int(self.i[1]) if self.i[1].isdigit() else vars[self.i[1]]
            return l | r
        elif self.op == 'LSHIFT':
            l = int(self.i[0]) if self.i[0].isdigit() else vars[self.i[0]]
            r = int(self.i[1]) if self.i[1].isdigit() else vars[self.i[1]]
            return l << r
        elif self.op == 'RSHIFT':
            l = int(self.i[0]) if self.i[0].isdigit() else vars[self.i[0]]
            r = int(self.i[1]) if self.i[1].isdigit() else vars[self.i[1]]
            return l >> r


    def __repr__(self):
        if not self.op:
            return self.i[0] + " -> " + self.o
        elif self.op == 'NOT':
            return "NOT "+self.i[0] + " -> " + self.o
        else:
            return self.i[0] + " " + self.op + " " + self.i[1] + " -> " + self.o


cmds = []
for l in open('day-07.input', 'r').readlines():
    cmds.append(C(l.strip()))

res = {}
while len(cmds) > 0:
    remove = []
    for i, c in enumerate(cmds):
        ready = True
        for _i in c.i:
            if _i.isdigit():
                continue
            elif _i not in res:
                ready = False
                break
        if not ready:
            continue
        res[c.o] = c.run(res)
        remove.append(i)
    if len(remove) == 0:
        raise Exception("nothing to remove !")
    for i in reversed(remove):
        del cmds[i]

print(res['a'])