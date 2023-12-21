import re

i_workflows, _ = open('day-19.input', 'r').read().split('\n\n')
f_map = 'xmas'

w = {}
a_nodes = []


class Node:
    pass


class TNode(Node):

    def __init__(self, parent, cond):
        self.parents = [(parent, cond)]

    def __eq__(self, other):
        return type(other) == type(self)


class A(TNode):

    def __init__(self, parent, cond):
        super().__init__(parent, cond)
        a_nodes.append(self)

    def __repr__(self):
        return 'A'


class R(TNode):

    def __repr__(self):
        return "R"


class Cmp(Node):

    def __init__(self, parent, cond, tokens):
        self.parents = [(parent, cond)]
        left = tokens.pop(0)
        assert left in f_map
        self.left = f_map.find(left)
        tokens.pop(0)
        limit = tokens.pop(0)
        assert limit.isdigit()
        self.limit = int(limit)
        assert tokens.pop(0) == ':'
        n_true = tokens.pop(0)
        if n_true not in ('A', 'R') and n_true not in w:
            raise KeyError(n_true)
        assert tokens.pop(0) == ','
        if tokens[0] not in ('A', 'R') and not (len(tokens) > 1 and tokens[1] in '<>') and tokens[0] not in w:
            raise KeyError(tokens[0])

        if len(tokens) > 1 and tokens[1] in '<>':
            self.false = GT(self, False, tokens) if tokens[1] == '>' else LT(self, False, tokens)
        else:
            n_false = tokens.pop(0)
            assert len(tokens) == 0
            if n_false in ('A', 'R'):
                self.false = A(self, False) if n_false == 'A' else R(self, False)
            else:
                self.false = w[n_false]
                w[n_false].parents.append((self, False))

        if n_true in ('A', 'R'):
            self.true = A(self, True) if n_true == 'A' else R(self, True)
        else:
            self.true = w[n_true]
            w[n_true].parents.append((self, True))


class LT(Cmp):

    def __repr__(self):
        return f"{self.left} < {self.limit}"

    def filter(self, allowed, cond):
        if cond:
            allowed[self.left][1] = min(self.limit - 1, allowed[self.left][1])
        else:
            allowed[self.left][0] = max(self.limit, allowed[self.left][0])
        return allowed


class GT(Cmp):

    def __repr__(self):
        return f"{self.left} > {self.limit}"

    def filter(self, allowed, cond):
        if cond:
            allowed[self.left][0] = max(self.limit + 1, allowed[self.left][0])
        else:
            allowed[self.left][1] = min(self.limit, allowed[self.left][1])
        return allowed


class Workflow(Node):

    def __init__(self, name, tokens):
        self.name = name
        self.parents = []
        assert tokens[1] in '<>'
        if tokens[1] == '<':
            self.start = LT(self, None, tokens)
        elif tokens[1] == '>':
            self.start = GT(self, None, tokens)

    def __repr__(self):
        return self.name


wq = i_workflows.split('\n')
while wq:
    i_workflow = wq.pop(0)
    w_name, w_data = i_workflow[:-1].split('{')
    try:
        w[w_name] = Workflow(w_name, re.split('([<>:,])', w_data))
    except KeyError:
        wq.append(i_workflow)

all_allowed = []
for a in a_nodes:
    states = [([[1, 4000], [1, 4000], [1, 4000], [1, 4000]], a.parents)]
    while states:
        allowed, parents = states.pop(0)
        for parent, cond in parents:
            if type(parent) is Workflow:
                if parent.name == 'in':
                    all_allowed.append(allowed)
                else:
                    states.insert(0, ([a.copy() for a in allowed], parent.parents))
            else:
                n_allowed = parent.filter([a.copy() for a in allowed], cond)
                states.insert(0, (n_allowed, parent.parents))

r = 0
for a in all_allowed:
    cr = 1
    for i in range(4):
        cr *= (a[i][1] - a[i][0] + 1)
    r += cr
print(r)
