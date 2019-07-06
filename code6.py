#staircase
#link : https://www.hackerrank.com/challenges/staircase/problem



import sys

def staircase(n):
    i=n-1
    for j in range(1,n+1):
        print((" "*i)+("#"*j))
        i-=1
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
