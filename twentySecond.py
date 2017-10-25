from collections import Counter
x = input()
L = [int(i) for i in raw_input().split()]
n = input()
D = Counter(L)
sum = 0
for i in range(n):
    shoe, price = map(int, raw_input().split())
    if D[shoe] != 0:
        sum += price
        D[shoe] -= 1
print sum
