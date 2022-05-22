import sys
input=sys.stdin.readline

n=int(input())
l=sorted(map(int, input().split()))
x=int(input())

ans=0
start,end=0,n-1
while start<end:
    s=l[start]+l[end]
    if s==x: ans+=1; start+=1
    elif s>x: end-=1
    else: start+=1
    
print(ans)