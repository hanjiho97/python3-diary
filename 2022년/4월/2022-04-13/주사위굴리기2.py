import sys
from collections import deque
input=sys.stdin.readline

N,M,K=map(int, input().split())
MAP=[list(map(int, input().split())) for _ in range(N)]
score=[[0]*M for _ in range(N)]

def calculate(x, y):
    if score[x][y]: return score[x][y]
    cnt=1
    temp=[[x,y]]
    target=MAP[x][y]
    poslist=[]
    visited=[[False]*M for _ in range(N)]
    visited[x][y]=True
    while temp:
        x,y=temp.pop()
        poslist.append([x,y])
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M: continue
            if visited[nx][ny] or MAP[nx][ny]!=target: continue
            visited[nx][ny]=True
            temp.append([nx,ny])
            cnt+=1
    for x,y in poslist:
        score[x][y]=target*cnt
    return score[x][y]

dir=0
ans=0
cor=[0,0]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
diceUD=deque([2,1,5,6])
diceRL=deque([4,1,3,6])

def roll(dir):
    if dir==0:
        diceRL.rotate(1)
        diceUD[1],diceUD[-1]=diceRL[1],diceRL[-1]
    elif dir==1:
        diceUD.rotate(1)
        diceRL[1],diceRL[-1]=diceUD[1],diceUD[-1]
    elif dir==2:
        diceRL.rotate(-1)
        diceUD[1],diceUD[-1]=diceRL[1],diceRL[-1]
    elif dir==3:
        diceUD.rotate(-1)
        diceRL[1],diceRL[-1]=diceUD[1],diceUD[-1]

for _ in range(K):
    x,y=cor
    nx,ny=x+dx[dir],y+dy[dir]
    if 0<=nx<N and 0<=ny<M:
        cor[0],cor[1]=nx,ny
        ans+=calculate(nx,ny)
        roll(dir)
    else:
        if nx<0: nx+=2
        if nx>=N: nx-=2
        if ny<0: ny+=2
        if ny>=M: ny-=2
        cor[0],cor[1]=nx,ny
        ans+=calculate(nx,ny)
        dir=(dir+2)%4
        roll(dir)
    if diceUD[-1]>MAP[nx][ny]: dir=(dir+1)%4
    elif diceUD[-1]<MAP[nx][ny]: dir=(dir-1)%4
print(ans)