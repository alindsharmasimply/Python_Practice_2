import re


x = raw_input("Enter the expression ")
m = re.match('^Pa', x)
n = re.match('et$', x)

print m
print n
