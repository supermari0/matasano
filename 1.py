"""Converts hex string to base64."""
import base64
import sys

if __name__ == '__main__':
    hex_str = sys.argv[1]
    ascii_str = hex_str.decode('hex')
    base64_str = base64.b64encode(ascii_str)
    print(base64_str)
