#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    miny = 0
    maxy = 0
    print("list is ", arr)
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]= temp
    print(arr)

    miny = arr[0]+arr[1]+arr[2]+arr[3]
    maxy = arr[1]+arr[2]+arr[3]+arr[4]

    print('{} {}'.format(miny,maxy))

if __name__ == '__main__':
    arr = list(map(int, input('enter 5 int').rstrip().split()))

    miniMaxSum(arr)

