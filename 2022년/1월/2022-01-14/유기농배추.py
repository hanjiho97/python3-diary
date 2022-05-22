import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    temp=deque([[x,y]])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while temp:
        x, y = temp.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if data[nx][ny]==0:
                continue
            if data[nx][ny]==1:
                data[nx][ny]=0
                temp.append([nx,ny])


for _ in range(int(input())):
    M, N, K = map(int, input().split())

    data=[[0]*N for _ in range(M)]

    #데이터 받기
    for _ in range(K):
        x, y = map(int, input().split())
        data[x][y]=1

    ans=0
    for i in range(M):
        for j in range(N):
            if data[i][j]==1:
                bfs(i, j)
                ans+=1

    print(ans)