import sys
input = sys.stdin.readline

dp=[1]*31
for i in range(2, 31):
    dp[i]=dp[i-1]*i
for _ in range(int(input())):
    N, M = map(int, input().split())
    print(dp[M]//(dp[N]*dp[M-N]))