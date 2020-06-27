#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s):
    s = list(s)
    print(s)
    b = ''
    for i in range(len(s)):
        if i==0 or (s[i-1]==' 'and s[i]!= ' '):
            b=b+s[i].capitalize()
        elif s[i]==' ':
            b=b+s[i]
        elif s[i]!=' ':
            b=b+s[i]
        else: pass
    return b

if __name__ == '__main__':
    s = input('Enter Full name with one space separated between first name and last name')
    result = solve(s)
    print(result)