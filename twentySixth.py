from collections import deque
n = input()
for _ in range(n):
    i = input()
    maximum = 2 ** 31
    L = deque(map(int, raw_input().split()))
    for _ in range(len(L)):
        right = L[-1]
        left = L[0]
        if right >= left and right <= maximum:
            L.pop()
            maximum = right
        elif left >= right and left <= maximum:
            L.popleft()
            maximum = left
        else:
            break
    if len(L) == 0:
        print "Yes"
    else:
        print "No"
