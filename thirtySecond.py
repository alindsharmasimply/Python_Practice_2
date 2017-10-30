from __future__ import print_function
from itertools import product
A = map(int, raw_input().split())
B = map(int, raw_input().split())
print (*list(product(A, B)))
