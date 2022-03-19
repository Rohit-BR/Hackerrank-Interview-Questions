#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    p_r = 0
    n_r = 0
    z_r = 0
    
    for i in arr:
        if i <= -1:
            n_r += 1/n
        elif i >= 1:
            p_r += 1/n
        elif i == 0:
            z_r += 1/n
        else:
            continue
        
    print("{:.6f}".format(p_r))
    print("{:.6f}".format(n_r))
    print("{:.6f}".format(z_r))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
