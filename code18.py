#cat and mouse
#link : https://www.hackerrank.com/challenges/cats-and-a-mouse/problem




import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    a=(((z-x)**2)**0.5)
    b=(((z-y)**2)**0.5)
    if a<b:
        return "Cat A"
    elif a>b:
        return "Cat B"
    else:
        return "Mouse C"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
