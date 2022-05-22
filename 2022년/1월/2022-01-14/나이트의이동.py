import sys
from collections import deque
input = sys.stdin.readline

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def bfs(x0,y0,x,y):
    temp=deque([[x0,y0]])
    turn=0
    visit[x0][y0]=1
    while temp:
        l=len(temp)
        for _ in range(l):
            x1,y1=temp.popleft()
            if x1==x and y1==y:
                return turn
            for i, j in zip(dx,dy):
                nx=x1+i
                ny=y1+j
                if 0<=nx<I and 0<=ny<I:
                    if visit[nx][ny]==0:
                        visit[nx][ny]=1
                        temp.append([nx,ny])
        turn+=1

for _  in range(int(input())):
    I = int(input())
    visit=[[0]*I for _ in range(I)]
    x0, y0 = map(int, input().split())
    x, y = map(int, input().split())
    print(bfs(x0,y0,x,y))