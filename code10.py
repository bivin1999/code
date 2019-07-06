#grading students
#link : https://www.hackerrank.com/challenges/grading/problem



import sys

def solve(grades):
    c=[]
    for x in grades:
        m=x//5
        a=m*5
        b=x-a
        if b>=3 and x>=38:
            c.append(a+5)
        else:
            c.append(x)
    return tuple(c) 
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
