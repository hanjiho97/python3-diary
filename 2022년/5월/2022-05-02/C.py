import sys
input=sys.stdin.readline

dp=[0]*51
dp[0],dp[1]=1,1
for i in range(1,51):
    dp[i]=dp[i-1]*i

for _ in range(int(input())):
    s=input().rstrip()
    t=input().rstrip()
    if t=='a': print(1)
    elif 'a' not in t: 
        answer=0
        num=s.count('a')
        for i in range(1, num+1):
            answer+=dp[num]//(dp[i]*dp[num-i])
        print(answer+1)
    else: print(-1)
