#time conversion
#link : https://www.hackerrank.com/challenges/time-conversion/problem




import sys

def timeConversion(s):
    s1=s[8:]
    s2=s[:8]
    if s1=="AM":
        if s2[:2]=="12":
            return "00"+s2[2:]
        else:
            return s2
    else:
        if s2[:2]=="12":
            return s2
        else:
            return str(int(s2[:2])+12)+s2[2:]
s = input().strip()
result = timeConversion(s)
print(result)
