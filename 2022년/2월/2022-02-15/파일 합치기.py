#https://suri78.tistory.com/15
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K=int(input())
    file=list(map(int, input().split()))
    dp=[[0]*(K+1) for _ in range(K+1)]
    for i in range(1, K):
        dp[i][i+1]=file[i-1]+file[i]
        for j in range(i+2, K+1):
            dp[i][j]=dp[i][j-1]+file[j-1]

    for j in range(3, K+1):
        for i in range(j-2, 0, -1):
            temp=min([dp[i][i+k]+dp[i+k+1][j] for k in range(j-i)])
            dp[i][j]+=temp
    print(dp[1][K])
