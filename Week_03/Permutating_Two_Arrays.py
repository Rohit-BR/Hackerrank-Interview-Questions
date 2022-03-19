#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    A = sorted(A)
    A = list(reversed(A))
    B = sorted(B)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    else:
        return "YES"
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)
        print(result)
