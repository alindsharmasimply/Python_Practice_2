import re


def regex(s):
    print re.match('.|.', s)
    print re.match('g[golo]e', s)
    print re.match('[a-z][A-Z][0-9]', s)


regex('\n')
regex('goe')
regex('aB3')
