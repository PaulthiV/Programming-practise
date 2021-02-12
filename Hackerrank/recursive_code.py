#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)
    return fact

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
