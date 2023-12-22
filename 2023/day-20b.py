import sys
from math import lcm

class Module:

    def __init__(self, name):
        self.name = name
        self.c_high = 0
        self.c_low = 0
        self.children = []
        self.parents = []
        self.queue = []

    def send(self, high: bool):
        for c in self.children:
            if high:
                self.c_high += 1
            else:
                self.c_low += 1
            #print(f"{self.name} -{'high' if high else 'low'}-> {c.name}")
            c.queue.append((self, high))
        return self.children.copy()

    def __repr__(self):
        return f"{self.name}"
        #return f"{self.name} -> {','.join([c.name for c in self.children])}"


class Button(Module):

    def __init__(self, name):
        super().__init__(name)

    def process(self):
        return self.send(False)


class Broadcaster(Module):

    def __init__(self, name):
        super().__init__(name)

    def process(self):
        _, high = self.queue.pop(0)
        return self.send(high)


class FlipFlop(Module):

    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def process(self):
        _, high = self.queue.pop(0)
        if not high:
            self.state = not self.state
            return self.send(self.state)
        else:
            return []

    def __repr__(self):
        return f"%{super().__repr__()}"


class Conjunction(Module):

    def __init__(self, name):
        super().__init__(name)
        self.c_states = {}
        self.monitor = False
        self.m_data = {}

    def process(self):
        source, high = self.queue.pop(0)
        self.c_states[source.name] = high
        if self.monitor and high and source.name not in self.m_data:
            print(f"{source.name} : {b.c_low}")
            self.m_data[source.name] = b.c_low
        if all(self. c_states.values()):
            return self.send(False)
        else:
            return self.send(True)

    def __repr__(self):
        return f"&{super().__repr__()}"


class Empty(Module):

    def process(self):
        _, _ = self.queue.pop(0)
        return []


defs = [a.strip() for a in open('day-20.input', 'r').readlines()]
modules = {}

b = Button('button')
modules['button'] = b

for l in defs:
    cc = l.split(' -> ')
    if cc[0] == 'broadcaster':
        bc = Broadcaster(cc[0])
        modules[cc[0]] = bc
        modules['button'].children.append(bc)
    else:
        name = cc[0][1:]
        modules[name] = FlipFlop(name) if cc[0][0] == '%' else Conjunction(name)

for l in defs:
    cc = l.split(' -> ')
    m = modules[cc[0][1:] if cc[0][0] in "&%" else cc[0]]
    for ch in cc[1].split(", "):
        if ch in modules:
            nm = modules[ch]
        else:
            nm = Empty(ch)
            modules[ch] = nm
        m.children.append(nm)
        nm.parents.append(m)
        if type(nm) is Conjunction:
            nm.c_states[m.name] = False


rx = modules['rx']
assert len(rx.parents) == 1
assert type(rx.parents[0]) is Conjunction
rx.parents[0].monitor = True

while True:
    n = b.process()
    while n:
        n += n.pop(0).process()
    if len(rx.parents[0].m_data) == len(rx.parents[0].parents):
        break

print(lcm(*rx.parents[0].m_data.values()))
