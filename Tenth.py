import sys

#for an input of n = 100
n = int(raw_input().strip())
def fact(n):
    if n == 1:
        return 1
    n = n * fact(n-1)
    return n
print fact(n)