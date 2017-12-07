from textwrap import fill


def wrap(string, width):
    return fill(string, width)


print wrap(raw_input(), input())
