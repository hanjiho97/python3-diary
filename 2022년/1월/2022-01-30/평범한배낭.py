import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp=[[0]*(K+1) for _ in range(N)]

for i in range(N):
    for j in range(1, K+1):
        if j>=bag[i][0]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-bag[i][0]]+bag[i][1])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[N-1][-1])