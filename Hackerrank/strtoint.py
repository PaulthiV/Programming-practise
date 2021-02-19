#!/bin/python3

import sys


S = input().strip()


try:
    out = int(S)
    print(out)
except ValueError:
    print("Bad String")

    