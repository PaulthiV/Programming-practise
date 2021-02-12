#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    #print(steps, path)
    mount = 0
    valley = 0
    
    for i in path:

        if i == 'U':
            mount += 1
        if i == 'D':
            mount -= 1

        if i == 'U' and mount == 0:
            valley += 1

    return valley

if __name__ == '__main__':
    steps = int(input())
    path = input()

    print(countingValleys(steps, path))