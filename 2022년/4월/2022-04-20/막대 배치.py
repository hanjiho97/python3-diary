import sys
input =sys.stdin.readline

dp=[[[0]*21 for _ in range(21)] for _ in range(21)]
dp[1][1][1]=1
for n in range(2,21):
    for l in range(1,21):
        for r in range(1,21):
            dp[n][l][r]=dp[n-1][l-1][r]+dp[n-1][l][r-1]+(n-2)*dp[n-1][l][r]
for _ in range(int(input())):
    n,l,r=map(int, input().split())
    print(dp[n][l][r])