#mini-max sum
#link : https://www.hackerrank.com/challenges/mini-max-sum/problem




import sys

def miniMaxSum(arr):
    a=arr.copy()
    b=[]
    for x in arr:
        a.remove(x)
        b.append(sum(a))
        a=arr.copy()
    print(min(b),max(b))
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
