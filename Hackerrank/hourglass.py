#!/bin/python3

import math
import random
import re
import sys
import numpy as np
from array import *



if __name__ == '__main__':
    arr = np.array([[1,1,1,0,0,0],[0,1,0,0,0,0],
    [1,1,1,0,0,0],[0,0,2,4,4,0],
    [0,0,0,2,0,0],[0,0,1,2,4,0]])


hr_sum = []
for idx, x in np.ndenumerate(arr):
    #print(arr)
    temp = []
    #print(idx)
    row = idx[0]
    col = idx[1]
    #print(row,col)
    if arr[row:row+3,col:col+3].size == 9:

        newar = arr[row:row+3,col:col+3]

        newar = np.delete(newar,3)
        newar = np.delete(newar,4)

        #print(newar)
        #print(newar.sum())
        hr_sum.append(newar.sum())

#print(max(hr_sum))
hourglass = max(hr_sum)

temparr = []
for i in range(0,4):
    for j in range(0,4):
        sumarr = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
            arr[i+1][j+1] + \
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        #print(arr[i][j])
        #print(sumarr)
        temparr.append(sumarr)

print(max(temparr))

