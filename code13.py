#migratory birds
#link : https://www.hackerrank.com/challenges/migratory-birds/problem



import sys

def migratoryBirds(n, ar):
    a=[]
    b="".join(map(str,ar))
    for j in range(1,6):
        a.append(b.count(str(j)))
    i=a.index(max(a))
    return i+1
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
