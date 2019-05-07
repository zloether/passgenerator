#!/usr/bin/env python

###############################################################################################
# NAME: passgenerator.py
# 
# Website: https://github.com/zloether/passgenerator
#
# Description: Simple password generator written in Python. Can be imported or run by itself.
###############################################################################################


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from random import SystemRandom
import argparse
import os.path


# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------
upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers_chars = 'abcdefghijklmnopqrstuvwxyz'
number_chars = '0123456789'
special_chars = "-._~()'!*:@,;"
bundled_dictionary = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dictionary/words_english_6_char_plus.txt'))
default_phoenetic_length = 4



# -----------------------------------------------------------------------------
# generate gibberish password
# -----------------------------------------------------------------------------
def generate(length=32, upper=True, lower=True, numbers=True, special=True):
    alphabet = ''
    
    if upper:
        alphabet += upper_chars
    if lower:
        alphabet += lowers_chars
    if numbers:
        alphabet += number_chars
    if special:
        alphabet += special_chars
    
    rand = SystemRandom()

    while True:
        password = ''.join(rand.choice(alphabet) for i in range(length))
        if upper:
            if any(c in upper_chars for c in password):
                pass
            else:
                continue

        if lower:
            if any(c in lowers_chars for c in password):
                pass
            else:
                continue

        if numbers:
            if any(c in number_chars for c in password):
                pass
            else:
                continue

        if special:
            if any(c in special_chars for c in password):
                pass
            else:
                continue

        break
    
    return password



# -----------------------------------------------------------------------------
# generate phoenetic password
# -----------------------------------------------------------------------------
def phoenetic(number_words=4):
    words = [] # list to hold words

    # read dictionary file
    with open(bundled_dictionary, 'r') as f: # opens the file
        for line in f: # read file line by line
            words.append(line.strip()) # add each line to words list
    
    plist = [] # list to hold words in password
    rand = SystemRandom() # create Random object

    i = 0 # create iterator
    while i < number_words:
        r = rand.randrange(0, len(words)) # get random list index

        # make sure we haven't already picked that word
        if any(words[r] in p for p in plist):
            break

        plist.append(words[r]) # add word to password list
        i += 1 # iterate
    
    password_spaces = '' # create empty password with spaces for readability
    password = '' # create empty password

    # concatenate all the words together
    for i in plist:
        password_spaces = password_spaces + i + ' '
        password = password + i

    return password_spaces, password



# -----------------------------------------------------------------------------
# Configure argument parser
# -----------------------------------------------------------------------------
def __parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description='Generates secure random ' + \
                                    'passwords')
    
    # setup argument to store length
    parser.add_argument('length', nargs='?', default=32,
                        action='store', help='number of characters in length (default=32)')

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-l', '--lower-enable', dest='lower', default=True,
                        action='store_true', help="use lower case characters")
    
    # setup arugment to explicitly disable upper characters
    parser.add_argument('-L', '--lower-disable', dest='lower', default=None,
                        action='store_false', help="don't use lower case characters")

    # setup arugment to explicitly enable number characters
    parser.add_argument('-n', '--number-enable', dest='numbers', default=True,
                        action='store_true', help="use number characters")
    
    # setup arugment to explicitly enable number characters
    parser.add_argument('-N', '--number-disable', dest='numbers', default=None,
                        action='store_false', help="don't use number characters")
    
    # setup argument for phoenetic password
    parser.add_argument('-p', '--phoenetic', dest='phoenetic', default=False,
                        action='store_true', help='create phoenetic password using English words (default=4 words)')

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-s', '--special-enable', dest='special', default=True,
                        action='store_true', help="use special characters")
    
    # setup arugment to explicitly enable upper characters
    parser.add_argument('-S', '--special-disable', dest='special', default=None,
                        action='store_false', help="don't use special characters")

    # setup arugment to explicitly enable upper characters
    parser.add_argument('-u', '--upper-enable', dest='upper', default=True,
                        action='store_true', help="use upper case characters")
    
    # setup arugment to explicitly disable upper characters
    parser.add_argument('-U', '--upper-disable', dest='upper', default=None,
                        action='store_false', help="don't use upper case characters")
    
    # parse the arguments
    args = parser.parse_args()
    
    return args



# -----------------------------------------------------------------------------
# Run main
# -----------------------------------------------------------------------------
def __run_main():
    args = __parse_arguments()

    if args.phoenetic:
        #if args.length:
        #    password = phoenetic(args.length)
        #else:
        #    password = phoenetic(default_phoenetic_length)
        password_spaces, password = phoenetic(default_phoenetic_length)
        print(password_spaces)
        print(password)
        exit()
        


    if not args.upper and not args.lower and not args.numbers and not args.special:
        print('You have disabled all supported character sets. You must enable ' + \
                'at least one of the character sets to generate a password.')
        exit()
    
    try:
        length = int(args.length)
    except ValueError:
        print('Error: Input length "'+ args.length + '"is not a valid number')
        exit()

    password = generate(length=length, upper=args.upper, lower=args.lower,
                        numbers=args.numbers, special=args.special)
    print(password)



# -----------------------------------------------------------------------------
# Run interactively
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    __run_main()
