import collections
import sys
from collections import deque
input = sys.stdin.readline

#데이터 저장
M, N, H = map(int, input().split())
start=[]
target=0
data=[[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        data[i].append(list(map(int, input().split())))
        for k in range(M):
            if data[i][j][k]==1:
                start.append([i,j,k])
            if data[i][j][k]==0:
                target+=1

def bfs():
    temp=deque(start)
    global target
    day=0
    #이동할수 있는 방향
    dx=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dz=[0,0,0,0,1,-1]
    while temp and target:
        l=len(temp)
        for _ in range(l):
            z, y, x = temp.popleft()
            for i in range(6):
                nx=x+dx[i]
                ny=y+dy[i]
                nz=z+dz[i]
                if nx>=M or nx<0 or ny>=N or ny<0 or nz>=H or nz<0:
                    continue
                if data[nz][ny][nx]==0:
                    data[nz][ny][nx]=1
                    target-=1
                    temp.append([nz,ny,nx])
        day+=1
    if target:
        print(-1)
    else:
        print(day)

bfs()