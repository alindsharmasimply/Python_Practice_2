from collections import OrderedDict, Counter
n = input()
D = OrderedDict()
for i in range(n):
    s = raw_input()
    D[s] = D.get(s, 0) + 1
print len(D)
for g, p in D.items():
    print p,
