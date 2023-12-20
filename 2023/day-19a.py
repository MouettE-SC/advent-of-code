import re

i_workflows, i_parts = open('day-19.input', 'r').read().split('\n\n')

for i_workflow in i_workflows.split('\n'):
    print(i_workflow)
    w_name, w_data = i_workflow.split('{')
    w_data = w_data[:-1]
    print(w_name, re.split('([<>:,])', w_data))

for i_part in i_parts.split('\n'):
    p = {}
    for i, s in enumerate(i_part[1:-1].split(',')):
        p[i] = int(s.split('=')[1])