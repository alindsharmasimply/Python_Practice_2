from itertools import groupby
for j, k in groupby(raw_input()):
    print len(list(k)), j
