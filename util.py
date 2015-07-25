"""Utilities for the Matasano crypto challenges."""

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

