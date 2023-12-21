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
        self.parents = [parent, cond]
        left = tokens.pop(0)
        assert left in f_map
        self.left = f_map.find(left)
        tokens.pop(0)
        limit = tokens.pop(0)
        assert limit.isdigit()
        self.limit = int(limit)
        assert tokens.pop(0) == ':'
        n = tokens.pop(0)
        if n in ('A', 'R'):
            self.true = A(self, True) if n == 'A' else R(self, True)
        else:
            self.true = w[n]
            w[n].parents.append((self, True))
        assert tokens.pop(0) == ','
        if len(tokens) > 1 and tokens[1] in '<>':
            self.false = GT(self, False, tokens) if tokens[1] == '>' else LT(self, False, tokens)
            return
        n = tokens.pop(0)
        assert len(tokens) == 0
        if n in ('A', 'R'):
            self.false = A(self, False) if n == 'A' else R(self, False)
        else:
            self.false = w[n]
            w[n].parents.append((self, False))


class LT(Cmp):

    def __repr__(self):
        return f"{self.left} < {self.limit}"


class GT(Cmp):

    def __repr__(self):
        return f"{self.left} > {self.limit}"


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


for a in a_nodes:
    states = [([[1, 4000], [1, 4000], [1, 4000], [1, 4000]], a.parents)]
    while states:
        allowed, parents = states.pop(0)
        for parent in parents:
            pass




