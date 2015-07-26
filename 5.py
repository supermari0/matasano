"""Repeating key XOR. Function is implemented in util, an example of usage is
here."""
from util import xor_repeating

PLAINTEXT = ("Burning 'em, if you ain't quick and nimble\n"
             "I go crazy when I hear a cymbal")
KEY = 'ICE'

if __name__ == '__main__':
    print(xor_repeating(PLAINTEXT, KEY).encode('hex'))
