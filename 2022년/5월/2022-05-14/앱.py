import sys
input=sys.stdin.readline

N,M=map(int ,input().split())
memory=list(map(int, input().split()))
cost=list(map(int, input().split()))

size=sum(cost)
dp=[0]*(size+1)

for i in range(N):
    for j in range(size, cost[i]-1,-1):
        dp[j]=max(dp[j], dp[j-cost[i]]+memory[i])

for i in range(size+1):
    if dp[i]>=M: ans=i; break
print(ans)