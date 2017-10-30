n, m = map(int, raw_input().split())
array = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
sum = 0
for i in range(len(array)):
    if array[i] in A:
        sum += 1
    elif array[i] in B:
        sum -= 1
print sum
