n = input()
for i in range(n):
    s = raw_input()
    f = 0
    for j in range(1, (len(s) / 2) + 1):
        s1 = s[0: j]
        x = int(s1)
        y = x
        while len(s1) < len(s):
            s1 = s1 + str(x + 1)
            x += 1
        if len(s1) == len(s):
            if s1 == s:
                print "YES", y
                f = 1
                break
    if f == 0:
    	print "NO"