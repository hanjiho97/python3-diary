import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cand = deque([[i,j] for i in range(N) for j in range(i%2,N,2)])

def open(start):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    temp=deque([start])
    union=[start]
    sum=A[start[0]][start[1]]
    while temp:
        x,y=temp.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]: continue
            if L<=abs(A[nx][ny]-A[x][y])<=R:
                temp.append([nx,ny])
                union.append([nx,ny])
                visited[nx][ny]=1
                sum+=A[nx][ny]
    if len(union)>1:
        avg=sum//len(union)
        for x,y in union:
            A[x][y]=avg
            cand.append([x,y])
    return

day=0
while True:
    visited=[[0]*N for _ in range(N)]
    for _ in range(len(cand)):
        i,j=cand.popleft()
        if not visited[i][j]:
            visited[i][j]=1
            open([i,j])
    if cand: day+=1
    else : print(day); break