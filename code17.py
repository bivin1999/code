#counting values
#link : https://www.hackerrank.com/challenges/counting-valleys/problem




import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    m=0
    c=0
    for x in s:
        b=m
        if x=='D':
            m=m-1
        else:
            m=m+1
        if m==0 and b<m:
            c=c+1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
