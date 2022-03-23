#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a = sorted(a)
    l_sub = 0
    
    for i in range(len(a)):
        sub = 1
        for j in range(i+1,len(a)):
            if abs(a[i]-a[j]) <= 1:
                sub += 1
        if sub >= l_sub:
            l_sub = sub
        
    return l_sub

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
