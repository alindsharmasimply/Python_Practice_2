def split_and_join(line):
    line = line.split()
    line = '-'.join(line)
    print line


split_and_join(raw_input())
