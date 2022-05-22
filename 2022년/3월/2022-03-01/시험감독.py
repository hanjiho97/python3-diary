import sys
input = sys.stdin.readline

N = int(input())
num = map(int, input().split())
B, C = map(int, input().split())

ans=0
for n in num:
    n-=B
    ans+=1
    if n<=0: continue
    elif n%C: ans+=(1+n//C)
    else: ans+=n//C

print(ans)