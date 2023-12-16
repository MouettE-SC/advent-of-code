# taken from https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4nsdd/?utm_source=share&utm_medium=web2x&context=3
# I just don't get it ;-)

import re

input = open('day-19.input').read()

molecule = input.split('\n')[-1][::-1]
reps = {m[1][::-1]: m[0][::-1]
        for m in re.findall(r'(\w+) => (\w+)', input)}
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print(count)