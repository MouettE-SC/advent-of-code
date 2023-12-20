import re
from collections import defaultdict

i_workflows, i_parts = open('day-19.input', 'r').read().split('\n\n')
f_map = 'xmas'
w = defaultdict(list)


def parse_rule(tokens):
    res = []
    left = tokens.pop(0)
    assert left in f_map
    res.append(f_map.find(left))
    op = tokens.pop(0)
    assert op in '<>'
    res.append(op)
    limit = tokens.pop(0)
    assert limit.isdigit()
    res.append(int(limit))
    assert tokens.pop(0) == ':'
    if len(tokens) > 1 and tokens[1] in '<>':
        res.append(parse_rule(tokens))
    else:
        res.append(tokens.pop(0))
    assert tokens.pop(0) == ','
    if len(tokens) > 1 and tokens[1] in '<>':
        res.append(parse_rule(tokens))
    else:
        res.append(tokens.pop(0))
    return res


def _run(w_data, part) -> bool:
    l1 = part[w_data[0]]
    op = w_data[1]
    r1 = w_data[2]

    if op == '>':
        if l1 > r1:
            n = w_data[3]
        else:
            n = w_data[4]
    else:
        if l1 < r1:
            n = w_data[3]
        else:
            n = w_data[4]

    if type(n) == list:
        return _run(n, part)
    elif n == 'A':
        return True
    elif n == 'R':
        return False
    else:
        return run_workflow(n, part)


def run_workflow(name, part) -> bool:
    return _run(w[name], part)


for i_workflow in i_workflows.split('\n'):
    w_name, w_data = i_workflow.split('{')
    w_data = w_data[:-1]
    w[w_name] += parse_rule(re.split('([<>:,])', w_data))

r = 0
for i_part in i_parts.split('\n'):
    p = {}
    for i, s in enumerate(i_part[1:-1].split(',')):
        p[i] = int(s.split('=')[1])
    if run_workflow('in', p):
        r += sum(p.values())
print(r)