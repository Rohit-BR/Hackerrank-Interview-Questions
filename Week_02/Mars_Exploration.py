#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here

    signal_length = len(s)
    expected_signal = "SOS" * (signal_length//3)
    changed_letters = 0
    
    for i in range(signal_length):
        if s[i] != expected_signal[i]:
            changed_letters +=1
            
    return changed_letters
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
