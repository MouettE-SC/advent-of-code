r = {}

for l in [a.strip() for a in open('day14.input').readlines()]:
    cc = l.split()
    r[cc[0]] = (int(cc[3]), int(cc[6]), int('-'+cc[13]))

st = {}
for k in r.keys():
    st[k] = [0, 0, 0]

for i in range(0, 2503):
    for k, v in r.items():
        if 0 <= st[k][1] < r[k][1]:
            st[k][0] += r[k][0]
        elif st[k][1] == r[k][1]:
            st[k][1] = r[k][2]
        st[k][1] += 1
    m = 0
    for k, v in st.items():
        m = max(m, v[0])
    for k, v in st.items():
        if v[0] == m:
            v[2] += 1

t = 0
for k, v in st.items():
    t = max(t, v[2])
print(t)
