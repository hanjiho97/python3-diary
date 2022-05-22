import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp=[0]*n
dp[0]=data[0]
ans=dp[0]

for i in range(1, len(data)):
    dp[i]=max(data[i], dp[i-1]+data[i])
    ans=max(ans, dp[i])

print(ans)