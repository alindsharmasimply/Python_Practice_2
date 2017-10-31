from __future__ import print_function
from itertools import permutations
s, space, r = raw_input().rpartition(' ')
s = list(permutations(sorted(list(s)), int(r)))
for i in s:
    print (*i, sep = '')
