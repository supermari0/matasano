"""XORs two equal length hex buffers."""
import sys
import util

if __name__ == '__main__':
    # Decode hex strings to ASCII first
    xs = sys.argv[1].decode('hex')
    ys = sys.argv[2].decode('hex')
    print(util.xor_ascii(xs, ys).encode('hex'))
