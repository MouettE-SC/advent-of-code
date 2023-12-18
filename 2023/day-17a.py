from heapq import heappop, heappush

grid = []
for i, l in enumerate(open('day-17.input', 'r').readlines()):
    grid.append([])
    for c in l.strip():
        grid[i].append(int(c))

nodes = {}
h = []


class Node:

    def __init__(self, i: int, j: int, direction: str, moves: int):
        self.i = i
        self.j = j
        self.distance = 2**32
        self.direction = direction
        self.moves = moves
        self.seen = False
        self._next = None

    def __repr__(self):
        return f"({self.i}, {self.j}, {self.direction}, {self.moves} : {self.distance})"

    def __hash__(self):
        return hash((self.i, self.j, self.direction, self.moves))

    def next(self):
        if self._next is not None:
            return self._next
        n = []
        if self.direction == 'UP' or self.direction == 'DOWN':
            if self.direction == 'UP' and self.moves <= 2 and self.i > 0:
                n.append((self.i-1, self.j, 'UP', self.moves + 1))
            elif self.direction == 'DOWN' and self.moves <= 2 and self.i < len(grid) - 1:
                n.append((self.i + 1, self.j, 'DOWN', self.moves + 1))
            if self.j > 0:
                n.append((self.i, self.j-1, 'LEFT', 1))
            if self.j < len(grid[self.i]) - 1:
                n.append((self.i, self.j + 1, 'RIGHT', 1))
        elif self.direction == 'LEFT' or self.direction == 'RIGHT':
            if self.direction == 'LEFT' and self.j > 0 and self.moves <= 2:
                n.append((self.i, self.j - 1, 'LEFT', self.moves + 1))
            if self.direction == 'RIGHT' and self.moves <= 2 and self.j < len(grid[self.i]) - 1:
                n.append((self.i, self.j + 1, 'RIGHT', self.moves + 1))
            if self.i > 0:
                n.append((self.i-1, self.j, 'UP', 1))
            if self.i < len(grid) - 1:
                n.append((self.i + 1, self.j, 'DOWN', 1))
        self._next = []
        for k in n:
            if k in nodes:
                self._next.append(nodes[k])
            else:
                nn = Node(*k)
                nodes[k] = nn
                self._next.append(nn)
        return self._next


s1 = (0, 1, 'RIGHT', 1)
nodes[s1] = Node(*s1)
nodes[s1].distance = grid[0][1]
heappush(h, (0, *s1))
s2 = (1, 0, 'DOWN', 1)
nodes[s2] = Node(*s2)
nodes[s2].distance = grid[1][0]
heappush(h, (0, *s2))


while h:
    _, *k = heappop(h)
    k = tuple(k)
    node = nodes[k]
    if node.seen:
        continue
    for nn in node.next():
        k = (nn.i, nn.j, nn.direction, nn.moves)
        if node.distance + grid[nn.i][nn.j] < nn.distance:
            nn.distance = node.distance + grid[nn.i][nn.j]
            heappush(h, (nn.distance, nn.i, nn.j, nn.direction, nn.moves))
    node.seen = True


print(min([n for n in nodes.values() if n.i == len(grid)-1 and n.j == len(grid[i])-1],
          key=lambda n: n.distance).distance)
