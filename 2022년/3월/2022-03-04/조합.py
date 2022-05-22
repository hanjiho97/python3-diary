import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp=[1]*101

for i in range(2, 101):
    dp[i]=i*dp[i-1]

print(dp[n]//(dp[n-m]*dp[m]))