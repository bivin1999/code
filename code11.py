#breaking records
#link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem




import sys

def breakingRecords(score):
    n=len(score)
    s=score[0]
    m=score[0]
    k=0
    j=0
    for i in range(1,n):
        if s<score[i]:
            s=score[i]
            k+=1
        if m>score[i]:
            m=score[i]
            j+=1
    return k,j
if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
