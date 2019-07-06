#utopian tree
#link : https://www.hackerrank.com/challenges/utopian-tree/problem


import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    a=((n+1)//2)+1
    b=2**a
    if n&1==0:
        return b-1
    else:
        return b-2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
