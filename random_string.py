# -*- coding: utf-8 -*-

from __future__ import print_function
import string
import random


def random_string(n):

    alphabets = string.ascii_lowercase
    rand_alphabets = [random.choice(alphabets) for i in xrange(n)]
    rand_str = ''.join(rand_alphabets)

    return rand_str


if __name__ == '__main__':

    name = random_string(5)
    print(name)