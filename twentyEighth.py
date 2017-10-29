from __future__ import print_function
i = input()
A = set(map(int, raw_input().split()))
j = input()
B = set(map(int, raw_input().split()))
print (*sorted(A.difference(B).union(B.difference(A))), sep='\n')
