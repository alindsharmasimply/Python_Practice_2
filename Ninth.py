count = 0


def reverse_check(x, k):
    global count
    if(int(x) - int(x[::-1])) % k == 0:
    	count += 1


def main():
    i, j, k = raw_input().split()
    global count
    for x in range(int(i), int(j) + 1):
        reverse_check(str(x), int(k))
    print count


main()
