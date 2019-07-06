#bon apetit
#link : https://www.hackerrank.com/challenges/bon-appetit/problem




n,k=map(int,str(input()).split())
c=list(map(int,str(input()).split()))
b=int(input())
c.remove(c[k])
s=sum(c)//2
if b-s==0:
    print("Bon Appetit")
else:
    print(b-s)