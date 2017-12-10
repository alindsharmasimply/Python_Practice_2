n = input()
s = set(map(int, raw_input().split()))
k = input()
for i in range(k):
    eval('s.{0}({1})'.format(*raw_input().split() + ['']))
print sum(s)
