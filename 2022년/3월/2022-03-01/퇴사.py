import sys
input = sys.stdin.readline

N = int(input())
dp=[0]*(N+1)
sc=[]
for _ in range(N):
    sc.append(list(map(int, input().split())))

init=0
for i in range(N):
    init=max(init, dp[i])
    if i+sc[i][0]<=N:
        dp[i+sc[i][0]]=max(dp[i+sc[i][0]], init+sc[i][1])

print(max(dp))