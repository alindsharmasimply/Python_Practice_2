A = set(map(int, raw_input().split()))
n = input()
g = "True"
for _ in range(n):
    N = set(map(int, raw_input().split()))
    if A.union(N) == A and len(N) < len(A):
        pass
    else:
        g = "False"
print g
