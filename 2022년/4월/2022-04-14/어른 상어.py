import sys
from collections import deque
input=sys.stdin.readline

N,M,k=map(int, input().split())
num=M
shark=[[] for _ in range(M+1)]
priority=[0]+[[0] for _ in range(M)]
sea=[]
for i in range(N):
    sea.append(list(map(int, input().split())))
    for j in range(N):
        if sea[i][j]!=0: shark[sea[i][j]].append([i,j])
first=list(map(int, input().split()))
for i in range(M):
    shark[i+1].append(deque([shark[i+1][0][:]]))
    shark[i+1][0]+=[first[i]]
for i in range(4*M):
    priority[i//4+1].append(list(map(int, input().split())))
direction=[(0),(-1,0),(1,0),(0,-1),(0,1)]

sec=0
while sec<1000:
    sec+=1
    cand=[]
    for i in range(1, M+1):
        if not shark[i][0]: continue
        x,y=shark[i][0][0],shark[i][0][1]
        pre,flag=[],False
        for p in priority[i][shark[i][0][2]]:
            dx,dy=direction[p]
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if sea[nx][ny]==0:
                flag=True
                break
            elif sea[nx][ny]==i: pre.append([nx,ny,p])
        if flag:
            if [nx,ny] not in cand:
                shark[i][0]=[nx,ny,p]
                cand.append([nx,ny])
                shark[i][1].append([nx,ny])
            else: 
                shark[i][0]=[]; num-=1
        else:
            shark[i][0]=pre[0]
            nx,ny=pre[0][0],pre[0][1]
            shark[i][1].append([nx,ny])
    if num==1: print(sec); exit()
    for i in range(1, M+1):
        if sec>=k and shark[i][1]:
            x,y=shark[i][1].popleft()
            if [x,y] not in shark[i][1]: sea[x][y]=0
        if not shark[i][0]: continue
        x,y=shark[i][0][0],shark[i][0][1]
        sea[x][y]=i
print(-1)