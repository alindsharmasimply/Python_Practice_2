n = input()
s1 = set(map(int, raw_input().split()))
b = input()
s2 = set(map(int, raw_input().split()))
print len(s1.union(s2))
