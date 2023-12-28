km = {
    1: {'U': 1, 'L': 1, 'D': 4, 'R': 2},
    2: {'U': 2, 'L': 1, 'D': 5, 'R': 3},
    3: {'U': 3, 'L': 2, 'D': 6, 'R': 3},
    4: {'U': 1, 'L': 4, 'D': 7, 'R': 5},
    5: {'U': 2, 'L': 4, 'D': 8, 'R': 6},
    6: {'U': 3, 'L': 5, 'D': 9, 'R': 6},
    7: {'U': 4, 'L': 7, 'D': 7, 'R': 8},
    8: {'U': 5, 'L': 7, 'D': 8, 'R': 9},
    9: {'U': 6, 'L': 8, 'D': 9, 'R': 9}
}

code = ''
for l in [a.strip() for a in open('day-02.input', 'r').readlines()]:
    n = 5
    for c in l:
        n = km[n][c]
    code += str(n)

print(code)