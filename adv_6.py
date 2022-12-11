from main import read_file
import numpy as np
from collections import Counter


def process():
    file = read_file('adv/adv_6.txt')

    count = 0
    for key, letter in enumerate(file[0]):
        letters = file[0][key:key+14]
        if len(Counter(letters)) == 14:
            print(key+14)


if __name__ == '__main__':
    process()