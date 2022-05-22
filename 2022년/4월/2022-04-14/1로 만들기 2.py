import sys
input = sys.stdin.readline

N=int(input())
dp=[[] for _ in range(N+1)]
dp[1].append(1)
for i in range(2, N+1):
    dp[i].append(i)
    temp=dp[i-1]
    if i%3==0:
        if len(dp[i//3])<len(temp):
            temp=dp[i//3]
    if i%2==0:
        if len(dp[i//2])<len(temp):
            temp=dp[i//2]
    dp[i]+=temp
    
print(len(dp[N])-1)
print(*dp[N])