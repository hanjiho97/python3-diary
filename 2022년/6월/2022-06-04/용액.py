import sys
input = sys.stdin.readline
N=int(input())
liquid=sorted(map(int, input().split()))
total=10**10
ans=[0,0]
start,end=0,N-1
a,b=liquid[start],liquid[end]

while a<b:
    if abs(a+b)<total:
        total=abs(a+b)
        ans[0],ans[1]=a,b
    if abs(a)==abs(b): break
    elif abs(a)>abs(b): start+=1
    else: end-=1
    a,b=liquid[start],liquid[end]

print(*ans)