#!/bin/python3

import math
import os
import random
import re
import sys

def convert_binary(num):
    #print(bin(num))
    return(count_ones(bin(num)))

def count_ones(binary):
    stringl = str(binary[2:]).split("0")
    #print(stringl)

    temp = 0
    for i in stringl:
        addx = 0
        for x in i:
            addx += int(x)
        
        if addx > temp: temp = addx

    return(temp)


if __name__ == '__main__':
    n = int(input())
    print(convert_binary(n))
