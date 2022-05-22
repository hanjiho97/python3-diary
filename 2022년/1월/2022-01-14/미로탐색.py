import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

#데이터 저장
data=[]
for _ in range(N):
    data.append(list(map(int, input().rstrip())))

#최단거리탐색 bfs
def bfs(x,y):
    temp=deque([[x,y]])
    while temp:
        x, y = temp.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if data[nx][ny]==0:
                continue
            if data[nx][ny]==1:
                data[nx][ny]+=data[x][y]
                temp.append([nx,ny])
    return data[N-1][M-1]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))