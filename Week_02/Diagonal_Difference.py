#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    diagonal_1 = 0
    diagonal_2 = 0
    
    for i in range(len(arr)):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][len(arr)-i-1]
        
    if diagonal_2 > diagonal_1:
        return diagonal_2 - diagonal_1
    else:
        return diagonal_1 - diagonal_2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
