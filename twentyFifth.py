from __future__ import print_function
from collections import deque
n = input()
L = deque()
for _ in range(n):
    c = raw_input().split(' ')
    eval("L." + c[0] + "(" + str(*c[1:]) + ")")
print (*L)
