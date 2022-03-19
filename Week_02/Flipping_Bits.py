#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    n_b = bin(n)[2:]
    pad_bits = "0" * (32 - len(n_b))
    n_b = pad_bits + n_b
    f_b = ""
    f_d = 1
    
    for i in n_b:
        if int(i) == 1:
            f_b += "0"
        else:
            f_b += "1"
    
    return int(f_b, 2)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
