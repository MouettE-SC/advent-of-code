lines = open('day-05.input', 'r').readlines()

seeds = []
c_map = {}
seed_to_soil = {}
soil_to_fert = {}
fert_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_humid = {}
humid_to_loc = {}

for l in lines:
    if not l.strip():
        continue
    cc = l.split(':')
    if len(cc) == 2:
        if cc[0] == 'seeds':
            seeds = [int(a.strip()) for a in cc[1].strip().split()]
        elif cc[0] == 'seed-to-soil map':
            c_map = seed_to_soil
        elif cc[0] == 'soil-to-fertilizer map':
            c_map = soil_to_fert
        elif cc[0] == 'fertilizer-to-water map':
            c_map = fert_to_water
        elif cc[0] == 'water-to-light map':
            c_map = water_to_light
        elif cc[0] == 'light-to-temperature map':
            c_map = light_to_temp
        elif cc[0] == 'temperature-to-humidity map':
            c_map = temp_to_humid
        elif cc[0] == 'humidity-to-location map':
            c_map = humid_to_loc
    else:
        cc = l.split()
        c_map[int(cc[1])] = (int(cc[0]), int(cc[2]))

seed_to_soil = {k: v for k, v in sorted(seed_to_soil.items())}
soil_to_fert = {k: v for k, v in sorted(soil_to_fert.items())}
fert_to_water = {k: v for k, v in sorted(fert_to_water.items())}
water_to_light = {k: v for k, v in sorted(water_to_light.items())}
light_to_temp = {k: v for k, v in sorted(light_to_temp.items())}
temp_to_humid = {k: v for k, v in sorted(temp_to_humid.items())}
humid_to_loc = {k: v for k, v in sorted(humid_to_loc.items())}


def next(s: int, m: dict[int, tuple[int, int]]) -> tuple[int, int]:
    kl = list(m.keys())
    i = 0
    while i < len(kl):
        _min = kl[i]
        _max = kl[i] + m[kl[i]][1]-1
        if s < _min:
            return s, _min - 1
        if _min <= s <= _max:
            return m[kl[i]][0] + s - kl[i], _max
        i += 1
    return s, -1


def next_range(ls: list[tuple[int, int]], m: dict[int, tuple[int, int]]) -> list[tuple[int, int]]:
    r = []
    for s in ls:
        s1, s2 = s
        while s1 < s2:
            v, mx = next(s1, m)
            if mx == -1 or mx >= s2:
                r.append((v, v+s2-s1))
                break
            else:
                r.append((v, v+mx-s1))
                s1 = mx+1
    return r


t = 0
for i in range(0, len(seeds), 2):
    r = next_range([(seeds[i], seeds[i] + seeds[i+1])], seed_to_soil)
    r = next_range(r, soil_to_fert)
    r = next_range(r, fert_to_water)
    r = next_range(r, water_to_light)
    r = next_range(r, light_to_temp)
    r = next_range(r, temp_to_humid)
    r = next_range(r, humid_to_loc)
    for l, _ in r:
        if t == 0:
            t = l
        else:
            t = min(t, l)

print(t)