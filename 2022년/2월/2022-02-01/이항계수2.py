import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [1]*(N+1)

for i in range(2, N+1):
    dp[i]=dp[i-1]*i

print((dp[N]//(dp[N-K]*dp[K]))%10007)