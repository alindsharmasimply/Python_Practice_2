# print "Hello! Enter your name"
# x = raw_input()
# print "Your name is", x

print "Enter no. of 1 litre or less containers"
    x = input()
    print "Enter no. of more than 1 litre containers"
    y = input()
    print "%.2f" % ((x * 0.1) + (y * 0.25))


P = input()
for i in range(1, 4):
    print "%.2f" % (P * (1.04) ** i)


from math import *
x = input()
print log10(x)


from math import *
x = input()
print tan(radians(x))


x, y = map(int, raw_input().split())
print (x * 12 * 2.54) + (y * 2.54)


from math import *
r = input()
print "Area is = ", pi * r * r


day = 24 * 60 * 60
hour = 60 * 60
minute = 60
seconds = input()
DD = seconds / day
HH = (seconds % day) / hour
MM = ((seconds % day) % hour) / minute
SS = (((seconds % day) % hour) % minute)
print "%d:%02d:%02d:%02d" % (DD, HH, MM, SS)
