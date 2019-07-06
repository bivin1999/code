#birthday cake candles
#link : https://www.hackerrank.com/challenges/birthday-cake-candles/problem




import sys

def birthdayCakeCandles(n, ar):
    a=max(ar)
    s=str(ar)
    return s.count(str(a))
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
