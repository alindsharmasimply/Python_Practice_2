from __future__ import print_function
k = input()
L = map(int, raw_input().split())
a = set()
b = set()
for x in L:
    if x in a:
        b.add(x)
    else:
        a.add(x)
print (*a.difference(b))
