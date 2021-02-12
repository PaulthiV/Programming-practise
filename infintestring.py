#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(st, num):

    count = 0
    strlen = len(st)

    cstr = st.count('a')

    c1 = (num // strlen) * cstr

    lim = num % strlen
    rem = st[:lim]

    c2 = rem.count('a')

    count = c1 + c2

    print(count)


if __name__ == '__main__':
    s = 'a'
    n = 1000000000000
    repeatedString(s, n)