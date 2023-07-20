#!/usr/bin/env python3
from math import ceil

def printCipher(cipher):
    # print text in Letterblocks of 5
    return ' '.join(cipher[i:i + 5] for i in range(0, len(cipher), 5))


def encode(text, key):
    # create two arrays of empty strings
    length = len(key)
    helper_text = [''] * length

    # fill columns with the letters
    for i in range(len(text)):
        helper_text[i % length] += text[i]

    # sort the key alphabeticaly and save its old index
    sorted_key = sorted(enumerate(key), key=lambda x: x[1].lower())

    # sort the columns and create a cipher
    cipher = ''
    for i in range(length):
        number = sorted_key[i][0]
        cipher += helper_text[number]

    return cipher

def decode(text, key):
    # create helper variables
    key_length = len(key)
    text_length = len(text)
    col_max_len = ceil(text_length / key_length)
    num_short_cols = text_length % key_length

    # sort the key and add the length of every column to the list
    col_data = [(k[0], k[1], col_max_len if k[0] < num_short_cols else col_max_len-1) for k in enumerate(key)]
    sorted_col_data = sorted(col_data, key=lambda x: x[1].lower())

    # create the columns and fill them with the letters. Empty fields are given the placeholder none
    permuted = [None] * len(key)
    src_idx = 0
    for (idx, _, length) in sorted_col_data:
        permuted[idx] = list(text[src_idx:src_idx+length]) + [None]*(col_max_len-length)
        src_idx += length

    # assemble the string
    result = []
    for col in zip(*permuted):
        result += list(filter(lambda x: x is not None, col))

    return ''.join(result)


def main():
    # variables
    text = "Loremipsumdolorsitametconsecteturadipisicielit"
    key1 = "culpa"
    key2 = "laborum"

    # calling decode two times
    puffer = encode(text, key1)
    cipher = encode(puffer, key2)

    print(printCipher(cipher))

    # encode
    puffer = decode(cipher, key2)
    text = decode(puffer, key1)

    print(text)

if __name__ == "__main__":
    main()
