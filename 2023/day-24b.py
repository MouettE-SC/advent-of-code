import random

hails = []

for l in [a.strip() for a in open('day-24.input', 'r').readlines()]:
    cc = l.split(' @ ')
    hails.append((*(map(int, cc[0].split(', '))), *(map(int, cc[1].split(', ')))))

print(hails)

# rx, ry, rz, vx, vy and vz are the rock variables (we search)
# xn, yn, zn, vxn, vyn and vzn are the hails variables (we have a bunch of them)

# With t being the time the rock hits the hailstone :
# rx + t*vx = xn + t*vxn
# ry + t*vy = yn + t*vyn
# rz + t*vz = zn + t*vzn
#
# removing t which we don't need, we have the following equality :
#
# xn - rx    yn - ry    zn - rz
# -------- = -------- = --------
# vx - vxn   vy - vyn   vz - vzn

# Considering only the x,y plane (first two parts of the equality above) we have the following equation :
# (vy - vyn)*(xn - rx) = (yn - ry) * (vx - vxn)
#
# developing and regrouping constant values (rock variables), we obtain :
# ry*vx - vy*rx = vx*yn - yn*vxn + ry*vxn - vy*xn + vyn*xn - vyn*rx
#
# because the left parts is constant for all hailstones, we deduce the following equality with another hailstone m:
# vx*ym - ym*vxm + ry*vxm - vy*xm + vym*xm - vym*rx = vx*yn - yn*vxn + ry*vxn - vy*xn + vyn*xn - vyn*rx
#
# Now we regroup by our unknowns and we obtain this nice linear equation with four unknows :
# (vym - vyn)*rx + (vxn - vxm)*ry + (yn - ym)*vx + (xm - xn)*vy = vym*xm - ym * vxm + yn*vxn - vyn*xn
# this can be solved using 4 random hailstones, hoping we don't get any division by zero ;-)

rx = ry = rz = vx = vy = vz = 0


def pivot_gauss(factors, rights):
    for i in range(len(factors)):
        pivot = factors[i][i]
        for j in range(len(factors)):
            factors[i][j] /= pivot
        rights[i] /= pivot
        for k in range(len(factors)):
            if k == i:
                continue
            f = factors[k][i]
            for j in range(len(factors)):
                factors[k][j] -= f*factors[i][j]
            rights[k] -= f*rights[i]


def p1_solve_using(hails_sample):
    global rx, ry, vx, vy
    factors = [[0 for _ in range(4)] for _ in range(4)]
    rights = [0 for _ in range(4)]
    for i in range(4):
        xn, yn, _, vxn, vyn, _ = hails_sample[i]
        xm, ym, _, vxm, vym, _ = hails_sample[i+1]
        factors[i][0] = vym - vyn
        factors[i][1] = vxn - vxm
        factors[i][2] = yn - ym
        factors[i][3] = xm - xn
        rights[i] = vym*xm - ym*vxm + yn*vxn - vyn*xn
    pivot_gauss(factors, rights)
    rx = round(rights[0])
    ry = round(rights[1])
    vx = round(rights[2])
    vy = round(rights[3])


p1_solve_using([hails[i] for i in random.sample(range(len(hails)), 5)])


# now we only need rz and vz
# we know rx, ry, vx ,vy ; considering the left and right parts of the 3-way equality above, we have :
# (vz - vzn)*(xn - rx) = (vx - vxn)*(zn - rz)
#
# again, we regroup by our unknowns:
# (vx - vxn)*rz + (xn - rx)*vz = (xn - rx)*vzn + (vx - vxn)*zn
# knowing rx and vx, this can be solved with 2 random hailstones

def p2_solve_using(hails_sample):
    global rx, rz, vx, vz
    factors = [[0 for _ in range(2)] for _ in range(2)]
    rights = [0 for _ in range(2)]
    for i in range(2):
        xn, _, zn, vxn, _, vzn = hails_sample[i]
        xm, _, zm, vxm, _, vzm = hails_sample[i+1]
        factors[i][0] = vx - vxn
        factors[i][1] = xn - rx
        rights[i] = (xn - rx)*vzn + (vx - vxn)*zn
    pivot_gauss(factors, rights)
    rz = round(rights[0])
    vz = round(rights[1])


p2_solve_using([hails[i] for i in random.sample(range(len(hails)), 3)])

print(rx + ry + rz)
