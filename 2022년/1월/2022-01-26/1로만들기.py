import sys
input = sys.stdin.readline

#기초세팅
dp={1:0, 2:1}
N = int(input())

for i in range(3, N+1):
    dp[i]=min(dp[i//2]+i%2, dp[i//3]+i%3)+1
print(dp[N])