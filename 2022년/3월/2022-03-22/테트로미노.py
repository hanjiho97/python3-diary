import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans, MAX = 0, max(map(max,data))

def search(x, y, count, total):
    global ans
    if count==4:
        ans=max(ans, total)
        return
    if ans>=total+(4-count)*MAX:
        return
    for i in range(3):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=M or visited[nx][ny]: continue
        visited[nx][ny]=1
        if count==2:
            search(x,y, count+1, total+data[nx][ny])
        search(nx,ny, count+1, total+data[nx][ny])
        visited[nx][ny]=0

dx=[0,1,-1]
dy=[1,0,0]
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        search(i,j, 1, data[i][j])
        visited[i][j]=0
print(ans)