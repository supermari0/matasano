"""Find a string that has been encrypted by a single-character XOR from a list
of newline-separated hex strings (4.txt). Pick the ciphertext whose top-scoring
decryption according to English character frequencies has the highest
probability of being a real English string according to character frequencies.

Print the plaintext.
"""
import sys

from util import single_char_xor_top_string_and_score

if __name__ == '__main__':
    list_of_strs = open('4.txt').read().splitlines()

    top_score = 0
    top_str = ''
    for ctext in list_of_strs:
        ctext_ascii = ctext.decode('hex')
        (string, score, key) = solve_single_char_xor(ctext_ascii)
        if score > top_score:
            top_score = score
            top_str = string

    print(top_str)
