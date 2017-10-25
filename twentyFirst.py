from __future__ import print_function
n, m = map(int, raw_input().split())
rows = [[int(i) for i in raw_input().split()] for _ in range(n)]
k = input()
rows.sort(key=lambda row: row[k])
for i in rows:
    print (*i)
