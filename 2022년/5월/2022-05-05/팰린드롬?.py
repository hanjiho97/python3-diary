import sys
input=sys.stdin.readline

N=int(input())
num=[0]+list(map(int, input().split()))
M=int(input())

dp=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][i]=1

for i in range(1,N+1):
    s=1
    e=s+i
    while e<N+1:
        if num[s]==num[e]:
            if i==1: dp[s][e]=1
            elif dp[s+1][e-1]: dp[s][e]=1
        s,e=s+1,e+1

for _ in range(M):
    S,E=map(int, input().split())
    print(dp[S][E])