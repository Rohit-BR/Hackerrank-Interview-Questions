#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_aAY a as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    a = sorted(arr)
    min_sum = 0
    max_sum = 0
    
    for i in range(1, len(a)):
        max_sum += a[i]
        
    min_sum  = (max_sum - a[len(a)-1]) + a[0]
        
    print(min_sum, max_sum)
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
