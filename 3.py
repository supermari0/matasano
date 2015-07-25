"""Break a single-byte XOR cipher. Assuming each character in a hex string has
been XORed against one character, find the most likely key based on
English character frequencies. Print the resulting message."""
import string
import sys

from util import CHAR_FREQ

if __name__ == '__main__':
    ctext = sys.argv[1].decode('hex')

    top_score = 0
    top_str = ''
    for key in string.printable:
        score = 0
        new_str = ''
        for char in ctext:
            new_char = chr(ord(char) ^ ord(key)).lower()
            new_str += new_char
            score += CHAR_FREQ.get(new_char, 0)

        if score > top_score:
            top_score = score
            top_str = new_str

    print(top_str)
