import sys
input = sys.stdin.readline
s=input().rstrip()
l=len(s)
check=[[0]*l for _ in range(l)]
dp=[i+1 for i in range(l)]

for i in range(l):
    check[i][i]=1

for i in range(1,l):
    start=0
    end=start+i
    while end<l:
        if s[start]==s[end]:
            if i==1: check[start][end]=1
            elif check[start+1][end-1]: check[start][end]=1
        start,end=start+1,end+1

for i in range(l):
    for j in range(i,l):
        if i==0 and check[0][j]: dp[j]=1; continue
        if check[i][j]: 
            dp[j]=min(dp[j],dp[i-1]+1)
print(dp[l-1])