#diagonal difference
#link : https://www.hackerrank.com/challenges/diagonal-difference/problem



import sys

def diagonalDifference(a,n):
    s1=0
    s2=0
    for i in range(n):
        s1+=a[i][i]
        s2+=a[i][n-1-i]
    b=max(s1,s2)
    c=min(s1,s2)
    return b-c
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a,n)
    print(result)
