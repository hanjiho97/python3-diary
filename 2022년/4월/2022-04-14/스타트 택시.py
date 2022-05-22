import sys
from collections import deque
input=sys.stdin.readline

N,M,fuel=map(int, input().split())
area=[list(map(int, input().replace('1','-1').split())) for _ in range(N)]
x,y=map(int,input().split())
des,target=[0],0
for i in range(M):
    r1,c1,r2,c2=map(int,input().split())
    area[r1-1][c1-1]=i+1
    des.append([r2-1,c2-1])
    target+=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def driving(x,y):
    if area[x][y]!=0: return gotodes(x,y,area[x][y])
    global fuel
    oil,custom=0,[]
    temp=deque([[x,y]])
    visited=[[False]*N for _ in range(N)]
    visited[x][y]=True
    while temp:
        oil+=1
        if fuel-oil<=0: return False
        for _ in range(len(temp)):
            x,y=temp.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N: continue
                if visited[nx][ny] or area[nx][ny]==-1: continue
                temp.append([nx,ny])
                visited[nx][ny]=True
                if area[nx][ny]!=0: custom.append([nx,ny])
        if custom:
            custom.sort()
            x,y=custom[0]
            fuel-=oil
            return gotodes(x,y,area[x][y])
    return False

def gotodes(x,y,num):
    global fuel, target
    area[x][y]=0
    oil=0
    temp=deque([[x,y]])
    visited=[[False]*N for _ in range(N)]
    visited[x][y]=True
    while temp:
        oil+=1
        for _ in range(len(temp)):
            x,y=temp.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx==des[num][0] and ny==des[num][1]:
                    if fuel-oil<0: return False
                    fuel+=oil
                    target-=1
                    if target==0: return True
                    return driving(nx,ny)
                if nx<0 or nx>=N or ny<0 or ny>=N: continue
                if visited[nx][ny] or area[nx][ny]==-1: continue
                temp.append([nx,ny])
                visited[nx][ny]=True
    return False

if driving(x-1,y-1): print(fuel)
else: print(-1)