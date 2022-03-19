#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar = sorted(ar)
    n_pairs_each = {}
    n_pairs = 0
    
    for i in range(len(ar)):
        if ar[i] not in n_pairs_each:
            n_pairs_each[ar[i]] = 1
        else:
            n_pairs_each[ar[i]] += 1
            
    for i in n_pairs_each:
        n_pairs += n_pairs_each[i]//2
        
    print(n_pairs_each)
    return n_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
