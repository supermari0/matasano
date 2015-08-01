"""Break repeating-key XOR (Vigenere cipher)."""
import base64
import itertools
import math
import util

# Min and max key sizes we will try, in bytes (inclusive)
MIN_KEYSIZE = 2
MAX_KEYSIZE = 40

# Try the top N key sizes for the key, according to edit distance of first two
# KEYSIZE bytes of the ciphertext
N_KEYSIZES = 5

def break_and_transpose(text, size):
    # Break text into blocks of size length and transpose the byte
    # matrix. For example, with the text "abcde1234", size 3:
    # a, b, c    a, d, 2    a, b, c    a, d, 2
    # d, e, 1 -> b, e, 3 or d, e, 1 -> b, e, 3
    # 2, 3, 4    c, 1, 4    2, 3       c, 1, None
    # Returned as list of lists with None for missing chars.
    blocks = []

    while len(text) > 0:
        blocks.append(text[0:size])
        text = text[size:]

    return [list(elem) for elem in itertools.izip_longest(*blocks)]

if __name__ == '__main__':
    # Convert base64 to ASCII/bytes
    with open('6.txt') as f:
        ctext = f.read()
        ctext = base64.b64decode(ctext)

    # Find N_KEYSIZES_TO_TRY key sizes with the smallest edit distance between
    # the first and second KEYSIZE bytes of the ciphertext, according to bit
    # differences. These will be our guesses for the key length.
    # TODO Make this prettier, make it a utility.
    # TODO I think this might be biased towards small keys.
    lens_and_distances = []
    for key_len in range(MIN_KEYSIZE, MAX_KEYSIZE + 1):
        try:
            first_bytes = ctext[0:key_len]
            second_bytes = ctext[key_len:key_len * 2]
            third_bytes = ctext[key_len * 2: key_len * 3]
            fourth_bytes = ctext[key_len * 3: key_len * 4]
        except IndexError:
            # Don't try keys that are too long
            break
        edit_dist_1 = float(util.edit_dist(first_bytes, second_bytes)) / key_len
        edit_dist_2 = float(util.edit_dist(second_bytes, third_bytes)) / key_len
        edit_dist_3 = float(util.edit_dist(third_bytes, fourth_bytes)) / key_len
        avg = (edit_dist_1 + edit_dist_2 + edit_dist_3) / 3
        lens_and_distances.append((key_len, avg))

    best_keysizes = sorted(lens_and_distances, key=lambda tup: tup[1])[0:
            N_KEYSIZES]
    print(best_keysizes)

    for (keysize, score) in best_keysizes:
        # Break the ciphertext into blocks of size KEYSIZE, and transpose the
        # blocks so that the first char of the first block goes with first char
        # of second block, second chars go together, etc.
        transposed_blocks = break_and_transpose(ctext, keysize)
        full_key = ''

        # Next, solve each block as though it was single-character XOR to find
        # that part of the key. Put the best guesses for the single-character
        # keys together and use these to guess the actual key.
        for block in transposed_blocks:
            (_, _, key) = util.solve_single_char_xor(block)
            full_key += key
        # Correct plaintext isn't top result for the example (6.txt), but it's
        # in the output. :D
        print('Key: ' + full_key)
        print(util.xor_repeating(ctext, full_key))
