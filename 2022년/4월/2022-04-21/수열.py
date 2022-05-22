import sys
input=sys.stdin.readline

N,K=map(int, input().split())
tem=list(map(int, input().split()))
sum,prefix=0,[0]
for t in tem:
    sum+=t
    prefix.append(sum)
ans=prefix[K]-prefix[0]
for i in range(1,N-K+1):
    ans=max(ans,prefix[i+K]-prefix[i])
print(ans)