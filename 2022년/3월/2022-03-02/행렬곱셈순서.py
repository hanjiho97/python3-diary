import sys
input = sys.stdin.readline

N = int(input())
matrix=[]
dp=[[[0,0,0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    r, c = map(int, input().split())
    dp[i][i][0]=r
    dp[i][i][1]=c

for j in range(1, N):
    for i in range(j-1, -1, -1):
        temp=99999999999999
        for k in range(j-i):
            if temp>dp[i][i+k][2]+dp[i+k+1][j][2]+dp[i][i+k][0]*dp[i][i+k][1]*dp[i+k+1][j][1]:
                temp=dp[i][i+k][2]+dp[i+k+1][j][2]+dp[i][i+k][0]*dp[i][i+k][1]*dp[i+k+1][j][1]
                dp[i][j][0]=dp[i][i+k][0]
                dp[i][j][1]=dp[i+k+1][j][1]
        dp[i][j][2]=temp
print(dp[0][N-1][2])
