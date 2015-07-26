"""Utilities for the Matasano crypto challenges.

This has a lot of implementations for challenges that may be reused in other
challenges.
"""
import string

# Character frequency percentages for English from
# http://norvig.com/mayzner.html
CHAR_FREQ = {
        'e': 12.49,
        't': 9.28,
        'a': 8.04,
        'o': 7.64,
        'i': 7.59,
        'n': 7.23,
        's': 6.51,
        'r': 6.28,
        'h': 5.05,
        'l': 4.07,
        'd': 3.82,
        'c': 3.34,
        'u': 2.73,
        'm': 2.51,
        'f': 2.40,
        'p': 2.14,
        'g': 1.87,
        'w': 1.68,
        'y': 1.66,
        'b': 1.48,
        'v': 1.05,
        'k': 0.54,
        'x': 0.23,
        'j': 0.16,
        'q': 0.12,
        'z': 0.09,
        # Spaces are frequent, so just assume 5
        ' ': 5
}


def xor_ascii(xs, ys):
    # Convert ASCII chars to numbers and xor them, change them back to chars,
    # then construct a new ASCII string from the output.
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

def xor_repeating(ptext, key):
    # Repeating key XOR. Takes two ASCII strings, plaintext and key, and
    # sequentially XORs the plaintext with the key, returning result as another
    # ASCII string.
    expand_len = len(ptext) / len(key) + 1
    new_key = (key * expand_len)[:len(ptext)]
    ctext = map(xor_ascii, ptext, new_key)
    return ''.join(ctext)

def edit_dist(x, y):
    # Take two ASCII strings, x and y, and find edit distance (number of
    # different bits).

    # Alternative: Could just XOR and count the 1s, but this is just as easy.

    # Convert to binary representation. Can't use bin() because it strips
    # leading 0s.
    bin_x = ''.join(['{:08b}'.format(ord(x_chr)) for x_chr in x])
    bin_y = ''.join(['{:08b}'.format(ord(y_chr)) for y_chr in y])

    # Iterate over shortest string
    diff = 0
    for i in range(min(len(bin_x), len(bin_y))):
        if bin_x[i] != bin_y[i]:
            diff += 1

    # Count bit positions that exist in one but not the other
    diff += abs(len(bin_x) - len(bin_y))
    return diff

def single_char_xor_top_string_and_score(ctext):
    # Given a ciphertext decoded into its ASCII (or byte) representation, find
    # the top-scoring plaintext string according to English character
    # frequencies, assuming a single-character repeated XOR.
    top_score = 0
    top_str = ''
    for key in range(256):
        score = 0
        new_str = ''
        for char in ctext:
            new_char = chr(ord(char) ^ key).lower()
            new_str += new_char
            score += CHAR_FREQ.get(new_char, 0)

        if score > top_score:
            top_score = score
            top_str = new_str
    return (top_str, top_score)
