lines = open('day-005.input', 'r').readlines()

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


def next(s: int, m: dict[int, tuple[int]]):
    kl = list(m.keys())
    i = 0
    while i < len(kl):
        if s < kl[i]:
            return s
        if kl[i] <= s <= kl[i] + m[kl[i]][1]:
            return m[kl[i]][0] + s - kl[i]
        i += 1
    return s


t = 0
for i in range(0, len(seeds), 2):
    print(i)
    for s in range(seeds[i], seeds[i] + seeds[i+1]):
        r = next(s, seed_to_soil)
        r = next(r, soil_to_fert)
        r = next(r, fert_to_water)
        r = next(r, water_to_light)
        r = next(r, light_to_temp)
        r = next(r, temp_to_humid)
        r = next(r, humid_to_loc)
        if t == 0:
            t = r
        else:
            t = min(t, r)

print(t)