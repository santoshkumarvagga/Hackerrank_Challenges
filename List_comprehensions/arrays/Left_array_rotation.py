#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    if d>n:
        d = d % n

    len_a = len(a)

    l =[]

    if d >0 and len_a - d >= 2:
        for i in range(d,len_a):
                l.append(a[i])
    elif d>0 and len_a-d==1:
            l.append(a[d])
    elif len_a - d==0 or d==0:
        pass
    else:
        pass

    for j in range(0,d):
        l.append(a[j])
    for i in l:
        print(i, end = ' ')
