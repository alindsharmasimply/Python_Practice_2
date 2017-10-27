from collections import OrderedDict
n = input()
D = OrderedDict()
for i in range(n):
    s, space, p = (raw_input().rpartition(' '))
    D[s] = D.get(s, 0) + int(p)
for s, p in D.items():
    print s, p
