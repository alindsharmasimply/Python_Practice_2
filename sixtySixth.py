from collections import namedtuple
pp = namedtuple('pp', 'a, b')
p1 = pp(1, 2)
p2 = pp(2, 4)
print p1.a * p2.a
print p1.b * p2.b
