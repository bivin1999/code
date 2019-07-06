#repeated string
#link : https://www.hackerrank.com/challenges/repeated-string/problem






import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l=len(s)
    d=n%l
    c=n//l
    h=s.count('a')
    m=(h*c)+(s[:d].count('a'))
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
