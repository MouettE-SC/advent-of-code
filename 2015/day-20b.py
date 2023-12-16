target = int(open('day20.input').read())
houses = [0 for _ in range(0, int(target/11+1))]

for elf in range(1, len(houses)):
    for house, n in zip(range(elf, len(houses), elf), range(0, 50)):
        houses[house] += elf*11

for house in range(1, len(houses)):
    if houses[house] > target:
        print(house)
        break
