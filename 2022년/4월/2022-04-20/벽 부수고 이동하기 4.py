import sys
input=sys.stdin.readline

N,M=map(int, input().split())
MAP=[list(map(int, input().rstrip())) for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(i,j):
    cnt=1
    temp=[[i,j]]
    todo=[]
    while temp:
        x,y=temp.pop()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]: continue
            if MAP[nx][ny]!=0:
                visited[nx][ny]=True
                todo.append([nx,ny])
                continue
            visited[nx][ny]=True
            cnt+=1
            temp.append([nx,ny])
    for x,y in todo:
        MAP[x][y]+=cnt
        visited[x][y]=False
    return

visited=[[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if MAP[i][j]==0 and not visited[i][j]:
            visited[i][j]=True
            dfs(i,j)
for i in range(N):
    for j in range(M):
        MAP[i][j]%=10
    print(''.join(map(str, MAP[i])))