n = input()
L = []
for i in range(n):
    s = raw_input().split()
    command = s[0]
    para = s[1:]
    command += "(" + ",".join(para) + ")"
    eval("L." + command)
print L
