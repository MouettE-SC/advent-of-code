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
            if self.direction == 'UP' and self.moves <= 9 and self.i > 0:
                n.append((False, self.i-1, self.j, 'UP', self.moves + 1))
            elif self.direction == 'DOWN' and self.moves <= 9 and self.i < len(grid) - 1:
                n.append((False, self.i + 1, self.j, 'DOWN', self.moves + 1))
            if self.j >= 4:
                n.append((True, self.i, self.j - 4, 'LEFT', 4))
            if self.j < len(grid[self.i]) - 4:
                n.append((True, self.i, self.j + 4, 'RIGHT', 4))

        elif self.direction == 'LEFT' or self.direction == 'RIGHT':
            if self.direction == 'LEFT' and self.j > 0 and self.moves <= 9:
                n.append((False, self.i, self.j - 1, 'LEFT', self.moves + 1))
            if self.direction == 'RIGHT' and self.moves <= 9 and self.j < len(grid[self.i]) - 1:
                n.append((False, self.i, self.j + 1, 'RIGHT', self.moves + 1))
            if self.i >= 4:
                n.append((True, self.i - 4, self.j, 'UP', 4))
            if self.i < len(grid) - 4:
                n.append((True, self.i + 4, self.j, 'DOWN', 4))
        self._next = []
        for cd, *k in n:
            k = tuple(k)
            if k in nodes:
                self._next.append((cd, nodes[k]))
            else:
                nn = Node(*k)
                nodes[k] = nn
                self._next.append((cd, nn))
        return self._next


s1 = (0, 4, 'RIGHT', 4)
nodes[s1] = Node(*s1)
nodes[s1].distance = sum(grid[0][j] for j in range(1, 5))
heappush(h, (0, *s1))
s2 = (4, 0, 'DOWN', 4)
nodes[s2] = Node(*s2)
nodes[s2].distance = sum(grid[i][0] for i in range(1, 5))
heappush(h, (0, *s2))


while h:
    _, *k = heappop(h)
    k = tuple(k)
    node = nodes[k]
    if node.seen:
        continue
    for cd, nn in node.next():
        k = (nn.n, nn.j, nn.direction, nn.moves)
        if cd:
            try:
                if nn.direction == 'UP':
                    nd = node.distance + sum(grid[i][node.j] for i in range(node.n - nn.moves, node.n))
                elif nn.direction == 'LEFT':
                    nd = node.distance + sum(grid[node.n][j] for j in range(node.j - nn.moves, node.j))
                elif nn.direction == 'DOWN':
                    nd = node.distance + sum(grid[i][node.j] for i in range(node.n + 1, node.n + nn.moves + 1))
                elif nn.direction == 'RIGHT':
                    nd = node.distance + sum(grid[node.n][j] for j in range(node.j + 1, node.j + nn.moves + 1))
            except IndexError:
                print("oups")
        else:
            nd = node.distance + grid[nn.n][nn.j]
        if nd < nn.distance:
            nn.distance = nd
        heappush(h, (nn.distance, nn.n, nn.j, nn.direction, nn.moves))
    node.seen = True


print(min([n for n in nodes.values() if n.i == len(grid)-1 and n.j == len(grid[i])-1],
          key=lambda n: n.distance).distance)
