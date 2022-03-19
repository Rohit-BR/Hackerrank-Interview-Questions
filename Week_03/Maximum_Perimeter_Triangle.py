#!/bin/python3
from itertools import permutations

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
def maximumPerimeterTriangle(n,sticks):
    # Write your code here
    i = n-3
    while i >= 0 and (sticks[i] + sticks[i+1] <= sticks[i+2]) :
        i -= 1

    if i >= 0 :
        return (sticks[i],sticks[i+1],sticks[i+2])
    else :
        return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = sorted(int(i) for i in input().split())

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
