'''
XOR decryption
'''

from itertools import product, cycle


def xor(data, key):
    return ''.join(([chr(int(c1) ^ c2) for (c1, c2) in zip(data, cycle(key))]))


if __name__ == '__main__':
    common_words = {'the', 'this', 'is', 'was'}
    encrypted_chars = open('p059_cipher.txt').read().split(',')
    key_range = range(ord('a'), ord('z') + 1)
    keys = list(product(key_range, repeat=3))
    for k in keys:
        decrypted_text = xor(encrypted_chars, k)
        if common_words & set(decrypted_text.split(' ')) == common_words:
            ascii_total = sum([ord(c) for c in decrypted_text])
            print("Decrypted text: {}\n\nASCII total is {}"
                  .format(decrypted_text, ascii_total))
            break
