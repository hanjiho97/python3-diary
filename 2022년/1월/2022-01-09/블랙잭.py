import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = sorted(map(int, input().split()), reverse=True)

ans=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            sum=s[i]+s[j]+s[k]
            if(sum<=M):
                if(sum>ans):
                    ans=sum
                break
print(ans)