#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #string_ints = [str(int) for int in ar]

    freq = {}
    for items in ar:
        freq[items] = ar.count(items)
    print(freq)

    pairs = 0
    for key, value in freq.items():
        pairs += (value//2)

    return pairs 

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

