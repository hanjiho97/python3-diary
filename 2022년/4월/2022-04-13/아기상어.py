import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
space=[]
for i in range(N):
    space.append(list(map(int, input().split())))
    for j in range(N):
        if space[i][j]==9:
            space[i][j]=0
            shark=[i,j]

def eat(shark, size, cnt, time):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited=[[False]*N for _ in range(N)]
    visited[shark[0]][shark[1]]=True
    sec=0
    eatable=[]
    temp=deque([shark])
    while temp:
        sec+=1
        for _ in range(len(temp)):
            x,y=temp.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N: continue
                if visited[nx][ny] or space[nx][ny]>size: continue
                visited[nx][ny]=True
                temp.append([nx,ny])
                if 0<space[nx][ny]<size: eatable.append([nx,ny])
        if eatable:
            eatable.sort()
            x,y=eatable[0]
            space[x][y]=0
            shark=[x,y]
            cnt+=1
            time+=sec
            if cnt==size: cnt=0; size+=1
            return eat(shark, size, cnt, time)
    print(time)
    return

eat(shark,2,0,0)