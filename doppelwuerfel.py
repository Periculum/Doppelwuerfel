#!/usr/bin/env python3
from math import ceil
from argparse import ArgumentParser
import sys

class DoppelWuerfel:

    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2


    def printCipher(self, cipher):
        # print text in Letterblocks of 5
        return ' '.join(cipher[i:i + 5] for i in range(0, len(cipher), 5))


    def encode_step(self, text, key):
        # Variables
        length = len(key)
        transposed = [''] * length

        # fill columns with letters
        for i in range(len(text)):
            transposed[i % length] += text[i]

        # sort the key alphabeticaly and save its old index
        sorted_col_data = sorted(enumerate(key), key=lambda x: x[1].lower())

        # sort the columns and create a cipher
        cipher = ''
        for number, _ in sorted_col_data:
            cipher += transposed[number]

        return cipher

    def decode_step(self, text, key):
        # create helper variables
        key_length = len(key)
        text_length = len(text)
        col_max_len = ceil(text_length / key_length)
        num_long_cols = text_length % key_length

        # sort the key and add the length of every column to the list
        col_data = [(char_no, key_char, col_max_len if char_no < num_long_cols or num_long_cols == 0 else col_max_len - 1) for char_no, key_char in enumerate(key)]
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
        helper = self.decode_step(text, self.key2)
        plain_text = self.decode_step(helper, self.key1)
        return plain_text

    def encode(self, text):
        helper = self.encode_step(text, self.key1)
        cipher = self.encode_step(helper, self.key2)
        return cipher



def main():
    # parsing arguments
    parser = ArgumentParser(prog='Doppelwürfel', description='Anagrammisierte Verschlüsselung')
    parser.add_argument('operation', choices=['e', 'd'])
    parser.add_argument('text', help="Use \" around the text if you want to enter with spaces.")
    parser.add_argument('key1')
    parser.add_argument('key2')
    args = parser.parse_args()

    # remove all spaces and use just lower case
    text = args.text.lower().replace(" ","")
    # initialise the keywords
    chiffre = DoppelWuerfel(args.key1, args.key2)

    # decode or encode
    if args.operation == 'd':
        print(f'Plain Text: ', chiffre.decode(text))
    else:
        print(f'Chiffre: ', chiffre.printCipher(chiffre.encode(text)))


if __name__ == "__main__":
    main()
