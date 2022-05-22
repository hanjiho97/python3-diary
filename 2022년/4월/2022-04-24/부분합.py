import sys
input=sys.stdin.readline

N,S=map(int, input().split())
num=list(map(int, input().split()))

ans=10**5
summary,end=0,-1
for start in range(N):
    while summary<S and end<N-1:
        end+=1
        summary+=num[end]
    if summary>=S: ans=min(ans,end-start+1)
    summary-=num[start]
if ans==10**5: print(0)
else: print(ans)