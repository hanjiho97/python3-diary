import sys
input = sys.stdin.readline

N = int(input())
dp=[[0,0] for _ in range(N)]
stair=[]
for _ in range(N):
    stair.append(int(input()))

if N==1:
    print(stair[0])
else:
    #한칸 올라감
    dp[0][0]=stair[0]
    #한번에 두칸 올라감
    dp[1][0]=stair[1]
    #첫번째칸에서 한칸 올라감
    dp[1][1]=stair[1]+dp[0][0]

    for i in range(2,N):
        #두칸 올라감
        dp[i][0]=max(dp[i-2][0],dp[i-2][1])+stair[i]
        #한칸 올라감
        dp[i][1]=dp[i-1][0]+stair[i]

    print(max(dp[-1]))