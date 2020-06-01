#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    if N%2 == 1: # if odd
        print('Weird')
    else: # if even
        if N >= 2 and N <=5: # between 2 to 5 inclusive
            print('Not Weird')
        elif N in range (6, 21): # between 6 to 20 inclusve
            print('Weird')
        elif N > 20: # if more than 20
            print('Not Weird')


