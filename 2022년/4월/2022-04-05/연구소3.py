import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
lab=[]
virus=[]
target=0
for i in range(N):
    lab.append(list(map(int, input().split())))
    for j in range(N):
        if lab[i][j]==2: virus.append([i,j])
        if lab[i][j]==0: target+=1

def spread(lab, virus, target):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    sec=0
    while virus:
        if target==0: return sec      
        sec+=1                                                      
        num=len(virus)
        for _ in range(num):
            x,y = virus.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N or lab[nx][ny]==1 or lab[nx][ny]==3: continue
                if lab[nx][ny]==0: target-=1
                virus.append([nx,ny])
                lab[nx][ny]=3
    return 2500
 
ans=2500
for c in combinations(virus, M):
    temp=[l[:] for l in lab] 
    for x, y in c:
        temp[x][y]=3
    sec=spread(temp, deque(c), target)
    ans=min(ans, sec)
if ans==2500: print(-1)
else: print(ans)