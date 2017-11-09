n = input()
a = set(raw_input())
for i in range(n - 1):
    a = a.intersection(raw_input())
print len(a)
