#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    #print(q)
    P = list(range(1, max(q)+1))
    total = 0

    for i in range(len(q)-1, -1, -1):
        bribe = q[i] - (i + 1)
        if bribe > 2:
            return "Too chaotic"
        for j in range(max(0,q[i]-2,i)):
            if q[j] > q[i]:
                total += 1
    return total


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
