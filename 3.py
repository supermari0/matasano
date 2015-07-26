"""Break a single-byte XOR cipher. Assuming each character in a hex string has
been XORed against one character, find the most likely key based on
English character frequencies. Print the resulting message."""
import string
import sys

import util

if __name__ == '__main__':
    ctext = sys.argv[1].decode('hex')
    (top_str, top_score) = util.single_char_xor_top_string_and_score(ctext)
    print(top_str)
