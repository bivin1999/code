#divisible sum pairs
#link : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem




import sys

def divisibleSumPairs(n, k, ar):
    s=0
    for i in range(n-1):
        a=ar[i]
        for x in ar[i+1:]:
            if (a+x)%k==0:
                s+=1
    return s
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
