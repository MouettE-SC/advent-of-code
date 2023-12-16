lines = [l.strip() for l in open('day-007.input', 'r').readlines()]

order = 'J23456789TJQKA'


class Hand:

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        m = {}
        for c in self.cards:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        nb_j = m['J'] if 'J' in m else 0
        m = list(m.values())
        if len(m) == 1:
            self.strength = 6
        elif len(m) == 2:
            if nb_j > 0:
                self.strength = 6
            elif 1 in m:
                self.strength = 5
            elif 2 in m:
                self.strength = 4
        elif len(m) == 3:
            if 3 in m:
                if nb_j > 0:
                    self.strength = 5
                else:
                    self.strength = 3
            else:
                if nb_j == 2:
                    self.strength = 5
                elif nb_j == 1:
                    self.strength = 4
                else:
                    self.strength = 2
        elif len(m) == 4:
            if nb_j > 0:
                self.strength = 3
            else:
                self.strength = 1
        else:
            if nb_j > 0:
                self.strength = 1
            else:
                self.strength = 0

    def __lt__(self, c):
        if self.strength < c.strength:
            return True
        elif self.strength == c.strength:
            for c1, c2 in zip(self.cards, c.cards):
                if c1 == c2:
                    continue
                return order.index(c1) < order.index(c2)
            return False
        else:
            return False

    def __repr__(self):
        return self.cards + " " + str(self.bid)


hands = []

for l in lines:
    cc = l.split()
    hands.append(Hand(cc[0], int(cc[1])))

t = 0
i = 1
for h in sorted(hands):
    print(h.cards, h.strength)
    t += i*h.bid
    i += 1

print(t)
