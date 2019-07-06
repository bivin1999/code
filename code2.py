#Compare the Triplets
#link : https://www.hackerrank.com/challenges/compare-the-triplets/problem




import sys

def solve(a0, a1, a2, b0, b1, b2):
    A=[a0,a1,a2]
    B=[b0,b1,b2]
    s1=0
    s2=0
    for i in range(3):
        if A[i]>B[i]:
            s1+=1
        elif A[i]<B[i]:
            s2+=1
    return s1,s2

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
