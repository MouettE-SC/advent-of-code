
hails = []

for l in [a.strip() for a in open('day-24.input', 'r').readlines()]:
    cc = l.split(' @ ')
    hails.append((*(map(int, cc[0].split(', '))), *(map(int, cc[1].split(', ')))))


def get_params(x1, y1, dx, dy):
    x2 = x1 + dx
    y2 = y1 + dy
    return (y1-y2)/(x1-x2), (x2*y1-x1*y2)/(x2-x1)


bounds = ((200000000000000, 400000000000000), (200000000000000, 400000000000000))

r = 0
for i, (sx, sy, sz, sdx, sdy, sdz) in enumerate(hails):
    sa, sb = get_params(sx, sy, sdx, sdy)
    for dx, dy, dz, ddx, ddy, ddz in hails[i+1:]:
        da, db = get_params(dx, dy, ddx, ddy)
        # print(f'{sx}, {sy}, {sz} @ {sdx}, {sdy}, {sdz} <=> {dx}, {dy}, {dz} @ {ddx}, {ddy}, {ddz}')
        if sa == da:
            # print('parallel')
            continue
        ix = (db - sb)/(sa - da)
        iy = sa * ix + sb
        # print('{0:.3f}, {1:.3f} : '.format(ix, iy), end='')
        past_s = (ix < sx and sdx > 0) or (ix > sx and sdx < 0)
        past_d = (ix < dx and ddx > 0) or (ix > dx and ddx < 0)
        if past_s and past_d:
            # print('past S+D')
            pass
        elif past_s:
            # print('past S')
            pass
        elif past_d:
            # print('past D')
            pass
        elif bounds[0][0] <= ix <= bounds[0][1] and bounds[1][0] <= iy <= bounds[1][1]:
            r += 1
        else:
            pass

print(r)
