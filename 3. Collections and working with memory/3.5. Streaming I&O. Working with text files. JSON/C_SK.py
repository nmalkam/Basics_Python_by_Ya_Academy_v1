from sys import stdin

for line in stdin:
    if line[0] != '#':
        print(line.split('#')[0].rstrip('\n'))
