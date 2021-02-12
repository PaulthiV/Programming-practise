#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    num = int(input())
    
    phoneBook = {}

    for i in range(0,num):
        name, phone = input().split()
        phoneBook[name] = phone 

    query = []
    for i in range(0,num):
        try:
            value = input()
        except EOFError as e:
            break
        query.append(value)

    
    for i in query:
        if i in phoneBook:
            print(i+"="+phoneBook[i])
        else:
            print("Not found") 

