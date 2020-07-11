#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    smax = -12*10000
    for row in range(len(arr) - 2):
        for column in range(len(arr[row]) - 2):
            top = sum(arr[row][column:column+3])
            middle = arr[row + 1][column + 1]
            bottom = sum(arr[row+2][column:column+3])
            s = top + middle + bottom
            smax = max(s, smax)

    print(smax)