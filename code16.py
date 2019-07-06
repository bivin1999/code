#drawing book
#link : https://www.hackerrank.com/challenges/drawing-book/problem





import sys

def solve(n, p):
    a=p//2
    if n&1==0:
        b=(n+1-p)//2
    else:
        b=(n-p)//2
    return min(a,b)
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
