import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
data=[]
for _ in range(N):
    data.append(list(map(int, input().split())))

prob=[]
start=[]
for i in range(N):
    for j in range(M):
        if data[i][j]==0: prob.append([i,j])
        elif data[i][j]==2: start.append([i,j])

def bfs(start, area):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for s in start:
        temp=deque([s])
        while temp:
            x, y = temp.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=M: continue
                if area[nx][ny]==1 or area[nx][ny]==2: continue
                if area[nx][ny]==0:
                    area[nx][ny]=2
                    temp.append([nx,ny])
    count=0
    for a in area:
        count+=a.count(0)
    return count

ans=0
for com in combinations(prob, 3):
    temp=deepcopy(data)
    for cor in com:
        temp[cor[0]][cor[1]]=1
    ans=max(ans, bfs(start, temp))
print(ans)