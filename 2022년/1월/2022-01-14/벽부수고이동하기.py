import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph=[list(map(int, input().rstrip())) for _ in range(N)]
visit=[[[0,0] for _ in range(M)] for _ in range(N)]
visit[0][0][1]=1
dx=[1,-1,0,0]
dy=[0,0,1,-1]

#0이면 벽을 한번 뚫은 상태 1이라면 아직 벽을 한번 뚫을 수 있는 상태
#bfs
def bfs():
    temp=deque([[0,0,1]])
    while temp:
        x, y, z =temp.popleft()
        if x==N-1 and y==M-1:
            return visit[x][y][z]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            #벽이고 한번 뚫은 상태
            if graph[nx][ny]==0 and visit[nx][ny][z]==0:
                visit[nx][ny][z]=visit[x][y][z]+1
                temp.append([nx,ny,z])
            #길이고 아직 뚫을 기회가 남은 상태
            elif graph[nx][ny]==1 and z==1:
                visit[nx][ny][0]=visit[x][y][1]+1
                temp.append([nx, ny, 0])
    return -1
print(bfs())