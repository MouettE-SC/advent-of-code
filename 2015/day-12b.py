import json

t = 0


def analyse(start):
    global t
    if type(start) is list:
        for e in start:
            analyse(e)
    elif type(start) is dict:
        if 'red' in start.values():
            return
        for k, v in start.items():
            analyse(k)
            analyse(v)
    elif type(start) is int:
        t += start


data = json.load(open('day-12.input'))

analyse(data)
print(t)