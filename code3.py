#A Very Big Sum
#link : https://www.hackerrank.com/challenges/a-very-big-sum/problem


import sys

def aVeryBigSum(n, ar):
    return sum(ar)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)