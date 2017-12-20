from __future__ import print_function
from itertools import combinations_with_replacement
s, n = raw_input().split()
print list(combinations_with_replacement(s, int(n)))
