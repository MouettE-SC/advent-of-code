class N:
    def __init__(self, n):
        self.n = n
        self.next = None
        self.prev = None

i = 0
start = None
current = None
last = None
for c in open('day-09.input', 'r').readline():
    sz = int(c)
    if i % 2 == 0:
        f_id = int(i/2)
    else:
        f_id = -1
    for _ in range(sz):
        if start is None:
            current = N(f_id)
            start = current
        else:
            current.next = N(f_id)
            current.next.prev = current
            current = current.next
    last = current
    i += 1

while last is not None and last.n == -1:
    last = last.prev

def show():
    p = start
    while True:
        if p.n >= 0:
            print(p.n, end='')
        else:
            print('.', end='')
        if p.next:
            p = p.next
        else:
            break
    print()

def check():
    p = start
    while True:
        if p.n == -1:
            return p
        if p.next:
            p = p.next
        else:
            break
    return None

e = check()
while e is not None:
    e.n = last.n
    last = last.prev
    last.next = None
    e = check()

ret = 0
current = start
i = 0
while True:
    ret += i*current.n
    current = current.next
    if current is None:
        break
    i += 1

print(ret)