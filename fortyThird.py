from string import *
from random import *

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxy"

ll = ''


def user_input():
    global ll
    print "Enter v for vowel, c for consonant, l for any letter"
    ch = raw_input()
    if ch == 'v':
        ll += choice(vowels)
    elif ch == 'c':
        ll += choice(consonants)
    elif ch == 'l':
        ll += choice(ascii_lowercase)
    else:
        ll += ch
    return ll


def main():
    for i in range(3):
        print user_input()


main()
