import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

#데이터 저장
data=[]
start=[]
target=0
for i in range(N):
    data.append(list(map(int, input().split())))
    #익은 토마토 위치확인 및 익힐 토마토 갯수세기
    for j in range(M):
        if data[i][j]==1:
            start.append([i,j])
        if data[i][j]==0:
            target+=1
            

#bfs
def bfs(sp):
    day=0
    global target
    temp=deque(start)
    while temp and target:
        l=len(temp)
        for _ in range(l):
            x, y= temp.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue
                if data[nx][ny]==-1:
                    continue
                if data[nx][ny]==1:
                    continue
                if data[nx][ny]==0:
                    data[nx][ny]=1
                    target-=1
                    temp.append([nx,ny])
        day+=1
    if target:
        return -1
    else:
        return day

dx=[-1,1,0,0]
dy=[0,0,1,-1]

print(bfs(start))