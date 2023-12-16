t = 0
lines = open('day-001.input').readlines()

rs = {'one': '1',
      'two': '2',
      'three': '3',
      'four': '4',
      'five': '5',
      'six': '6',
      'seven': '7',
      'eight': '8',
      'nine': '9',
      '1': '1',
      '2': '2',
      '3': '3',
      '4': '4',
      '5': '5',
      '6': '6',
      '7': '7',
      '8': '8',
      '9': '9'}

for l in lines:
    l = l.strip()
    s = l
    r = ''
    i = 0
    while i < len(s):
        f = list(filter(lambda x: s[i:].startswith(x), rs.keys()))
        if f:
            s = s[0:i] + rs[f[0]] + s[i+1:]
            i += 1
        else:
            s = s[0:i] + s[i+1:]
    t += int(s[0] + s[-1])
print(t)
