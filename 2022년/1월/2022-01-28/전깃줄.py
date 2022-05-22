import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
#크기순으로 정렬
lines.sort()
dp=[1]*N

for i in range(1, N):
    for j in range(i):
        if lines[i][1]>lines[j][1]:
            dp[i]=max(dp[i], dp[j]+1)
print(N-max(dp))