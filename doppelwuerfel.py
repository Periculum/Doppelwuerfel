#!/usr/bin/env python3
from math import ceil
import sys

class DoppelWuerfel:

    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2


    def printCipher(self, cipher):
        # print text in Letterblocks of 5
        return ' '.join(cipher[i:i + 5] for i in range(0, len(cipher), 5))


    def encode_step(self, text, key):
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

    def decode_step(self, text, key):
        # create helper variables
        key_length = len(key)
        text_length = len(text)
        col_max_len = ceil(text_length / key_length)
        num_long_cols = text_length % key_length

        # sort the key and add the length of every column to the list
        col_data = [(k[0], k[1], col_max_len if k[0] < num_long_cols or num_long_cols == 0 else col_max_len - 1) for k in enumerate(key)]
        sorted_col_data = sorted(col_data, key=lambda x: x[1].lower())

        # create the columns and fill them with the letters. Empty fields are given the placeholder none
        permuted = [None] * key_length
        src_idx = 0
        for (idx, _, length) in sorted_col_data:
            permuted[idx] = list(text[src_idx:src_idx+length]) + [None] * (col_max_len - length)
            src_idx += length

        # assemble the string
        result = []
        for col in zip(*permuted):
            result += list(filter(lambda x: x is not None, col))

        return ''.join(result)


    def decode(self, text):
        puffer = self.decode_step(text, self.key2)
        plain_text = self.decode_step(puffer, self.key1)
        return plain_text

    def encode(self, text):
        puffer = self.encode_step(text, self.key1)
        cipher = self.encode_step(puffer, self.key2)
        return cipher



def main():
    # remove all spaces and use just lower case
    text = sys.argv[2].lower()
    text = text.replace(" ","")

    # initialise the keywords
    key1 = sys.argv[3]
    key2 = sys.argv[4]
    chiffre = DoppelWuerfel(key1, key2)

    # decode or encode
    if sys.argv[1] == 'd':
        print(f'Plain Text: ', chiffre.decode(text))
    elif sys.argv[1] == 'e':
        print(f'Chiffre: ', chiffre.printCipher(chiffre.encode(text)))
    else:
        print('Please choose (d)ecode or (e)ncode')


if __name__ == "__main__":
    main()
