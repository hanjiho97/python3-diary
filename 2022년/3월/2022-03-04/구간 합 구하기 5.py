import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp=[[0 for _ in range(N+1)]]
for i in range(1, N+1):
    d=[0]
    value=0
    for j, v in enumerate(map(int, input().split())):
        value+=v
        d.append(dp[i-1][j+1]+value)
    dp.append(d)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])