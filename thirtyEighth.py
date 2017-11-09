import sys


def minSteps(n, B):
    return B.count('010')


n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)
