#plus minus
#link : https://www.hackerrank.com/challenges/plus-minus/problem




import sys

def plusMinus(arr):
    a=0
    b=0
    c=0
    n=len(arr)
    for x in arr:
        if x>0:
            a+=1
        elif x<0:
            b+=1
        else:
            c+=1
    print(float(a)/n)
    print(float(b)/n)
    print(float(c)/n)
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
