N, n = int(raw_input()), raw_input().split()
print all([int(i) > 0 for i in n]) and any([x == x[::-1] for x in n])
