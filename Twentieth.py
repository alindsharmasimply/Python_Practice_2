n, x = map(int, raw_input().split())
scores = [map(float, raw_input().split()) for _ in range(x)]
for student in zip(*scores):
    print(sum(student) / x)
