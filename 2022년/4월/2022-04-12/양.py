import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int, input().split())
place=[input().rstrip() for _ in range(R)]
visited=[[False]*C for _ in range(R)]
sheep,wolf=0,0

def bfs(i, j):
    global sheep
    global wolf
    s,w=0,0
    temp=deque([[i,j]])
    while temp:
        x,y=temp.popleft()
        if place[x][y]=='v': w+=1
        elif place[x][y]=='o': s+=1
        if x+1<R and not visited[x+1][y] and place[x+1][y]!='#':
            visited[x+1][y]=True
            temp.append([x+1,y])
        if x-1>=0 and not visited[x-1][y] and place[x-1][y]!='#':
            visited[x-1][y]=True
            temp.append([x-1,y])
        if y+1<C and not visited[x][y+1] and place[x][y+1]!='#' :
            visited[x][y+1]=True
            temp.append([x,y+1])
        if y-1>=0 and not visited[x][y-1] and place[x][y-1]!='#':
            visited[x][y-1]=True
            temp.append([x,y-1])
    if s>w: sheep+=s
    else: wolf+=w

for i in range(R):
    for j in range(C):
        if not visited[i][j] and place[i][j]!='#':
            visited[i][j]=True
            bfs(i,j)
print('%d %d'%(sheep, wolf))