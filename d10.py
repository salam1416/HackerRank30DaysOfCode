#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin_str = ''
    while n != 0:
        bin_str = str(n%2) + bin_str 
        n = int(n/2)
        
cnt = 0
maxx = 0
for i in bin_str:
    if i == '1':
        cnt+=1
        if cnt > maxx:
            maxx = cnt
    else:
        cnt = 0



#print(bin_str)
print(maxx)