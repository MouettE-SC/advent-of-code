import random


class Node:

    def __init__(self, name):
        self.name = name
        self.links = {}
        self.size = 1

    def __repr__(self):
        return self.name


nodes = {}
for l in [a.strip() for a in open('day-25.input', 'r').readlines()]:
    source, dests = l.split(": ")
    for dest in dests.split():
        if source not in nodes:
            s = Node(source)
            nodes[source] = s
        else:
            s = nodes[source]
        if dest not in nodes:
            d = Node(dest)
            nodes[dest] = d
        else:
            d = nodes[dest]
        s.links[d] = 1
        d.links[s] = 1

nodes = nodes.values()


def copy():
    c_nodes = {}
    for o_s in nodes:
        if o_s.name not in c_nodes:
            s = Node(o_s.name)
            c_nodes[s.name] = s
        else:
            s = c_nodes[o_s.name]
        for o_d, c in o_s.links.items():
            if o_d.name not in c_nodes:
                d = Node(o_d.name)
                c_nodes[d.name] = d
            else:
                d = c_nodes[o_d.name]
            s.links[d] = c
            d.links[s] = c
    return list(c_nodes.values())


# implementation of Karger algorithm
def karger(k_nodes):
    step = 1
    while len(k_nodes) > 2:
        n1 = random.choice(k_nodes)
        n2 = random.choice(list(n1.links.keys()))
        sn = Node(f"{n1.name}-{n2.name}")
        sn.size = n1.size + n2.size
        for na, nb in (n1, n2), (n2, n1):
            for d, c in na.links.items():
                if d != nb:
                    if d in sn.links:
                        sn.links[d] += c
                    else:
                        sn.links[d] = c
                    if sn in d.links:
                        d.links[sn] += c
                    else:
                        d.links[sn] = c
                    del d.links[na]
        k_nodes.remove(n1)
        k_nodes.remove(n2)
        k_nodes.append(sn)
        step += 1


iterations = 1
while True:
    w_nodes = copy()
    karger(w_nodes)
    cut = list(w_nodes[0].links.values())[0]
    print(f"{iterations} : {cut}")
    if cut == 3:
        break
    iterations += 1

r = 1
for k in w_nodes:
    r *= k.size

print(r)
