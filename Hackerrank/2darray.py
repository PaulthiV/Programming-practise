#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],
    [1,1,1,0,0,0],[0,0,2,4,4,0],
    [0,0,0,2,0,0],[0,0,1,2,4,0]]
    
    sum = []


    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            
    print(max(sum))