import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data=[]
for i in range(N):
    data.append(input().replace('B', '0').replace('W','1'))

compare=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        compare[i][j]=int(data[i][j]==str((i+j)%2))

ans=32
for i in range(0, N+1-8):
    for j in range(0, M+1-8):
        count=0
        for k in range(0, 8):
            count+=sum(compare[k+i][j:j+8])
        ans=min(ans, count, 64-count)

print(ans)