from __future__ import print_function
from itertools import combinations_with_replacement
s, space, r = raw_input().rpartition(' ')
s = sorted(s)
print (*list(combinations_with_replacement(s, int(r))), sep='')
