import sys
input = sys.stdin.readline
 
n=int(input())
a=list(map(int, input().split()))
 
ans=10**30
for i in range(n):
    move=0
    pre=0
    for j in range(i+1,n):
        num=pre//a[j]+1
        move+=num
        pre=a[j]*num
    pre=0
    for j in range(i-1,-1,-1):
        num=pre//-a[j]+1
        move+=num
        pre=-a[j]*(num)
    ans=min(ans,move)
print(ans)