#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    jumps = 0
    length  = len(c)
    i = 0
    while i != length:
        #print('clouds:',c[i])

        if i+2<length and c[i] == c[i+2]:
            jumps += 1
            i += 2
        elif i+1<length and c[i] == c[i+1]:
            jumps += 1
            i += 1
        else:
            i += 1  
        #print('jumps', jumps)  
    return jumps

if __name__ == '__main__':

    n = 6

    c = [0, 0, 0, 0, 1, 0]

    result = jumpingOnClouds(c)
    print(result)
