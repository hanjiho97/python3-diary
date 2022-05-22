import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp=[[1,1] for _ in range(N)]
length=1

for i in range(1, N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i][0]=max(dp[i][0], dp[j][0]+1)
        elif A[i]<A[j]:
            dp[i][1]=max(dp[i][1], dp[j][1]+1, dp[j][0]+1)
    if length<max(dp[i]):
        length=max(dp[i])

print(length)