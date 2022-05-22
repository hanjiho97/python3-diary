#동적프로그래밍
import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
dp=[[0]*21 for _ in range(N)]
dp[0][number[0]]=1

for i in range(N-2):
    for j in range(21):
        if dp[i][j]:
            nextValue1=j+number[i+1]
            nextValue2=j-number[i+1]
            if 0<=nextValue1<=20:
                dp[i+1][nextValue1]+=dp[i][j]
            if 0<=nextValue2<=20:
                dp[i+1][nextValue2]+=dp[i][j]
print(dp[N-2][number[-1]])