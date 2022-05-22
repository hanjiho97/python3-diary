import sys
input = sys.stdin.readline

n = int(input())
dp=[[0,0] for _ in range(n)]

drink=[]
for _ in range(n):
    drink.append(int(input()))

if n==1:
    print(drink[0])
elif n==2:
    print(drink[0]+drink[1])
else:
    dp[0][0]=drink[0]
    dp[1][0]=drink[1]
    dp[1][1]=drink[0]+drink[1]
    dp[2][0]=drink[0]+drink[2]
    dp[2][1]=dp[1][0]+drink[2]

    for i in range(3, n):
        dp[i][0]=max(dp[i-2][0], dp[i-2][1], dp[i-3][0], dp[i-3][1])+drink[i]
        dp[i][1]=dp[i-1][0]+drink[i]

    print(max(*dp[-1], *dp[-2]))