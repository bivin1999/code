#day of the programmer
#link : https://www.hackerrank.com/challenges/day-of-the-programmer/problem



import sys

def solve(year):
    if year==1918:
        print("26.09.1918")
        return 0
    elif year>1918:
        if (year%400==0) or (year%4==0 and year%100!=0):
            print("12.09.%d"%year)
            return 0
    elif year%4==0:
        print("12.09.%d"%year)
        return 0
    print("13.09.%d"%year)
year = int(input().strip())
result = solve(year)
