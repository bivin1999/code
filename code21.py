#cut the sticks
#link : https://www.hackerrank.com/challenges/cut-the-sticks/problem



import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    a=[]
    n=len(arr)
    x=min(arr)
    i=arr.count(x)
    while i!=n:
        a.append(n)
        while i>0:
            arr.remove(x)
            i-=1
        x=min(arr)
        i=arr.count(x)
        n=len(arr)
    if n!=0:
        a.append(n)
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
