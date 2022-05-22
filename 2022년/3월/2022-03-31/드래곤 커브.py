import sys
from copy import deepcopy
input = sys.stdin.readline

dragon=[[] for _ in range(11)]
dragon[0]=[[0,0],[1,0]]
grid=[[0]*101 for _ in range(101)]

def rotate(curve):
    romal=[[0, 1],[-1, 0]]
    for i in range(len(curve)):
        a=romal[0][0]*curve[i][0]+romal[0][1]*curve[i][1]
        b=romal[1][0]*curve[i][0]+romal[1][1]*curve[i][1]
        curve[i][0],curve[i][1] = a,b
    return curve

def next_gen(dragon):
    temp=deepcopy(dragon)
    newdragon=deepcopy(dragon)
    temp=rotate(temp)
    tarx,tary = dragon[-1]
    curx,cury = temp.pop()
    for i in range(len(temp)-1, -1, -1):
        newdragon.append([temp[i][0]+(tarx-curx), temp[i][1]+(tary-cury)])
    return newdragon

for i in range(1, 11):
    dragon[i]=next_gen(dragon[i-1])

N = int(input())
for _ in range(N):
    x,y,d,g = map(int, input().split())
    temp=deepcopy(dragon[g])
    if d==0:
        romal=[[1,0],[0,1]]
    elif d==1:
        romal=[[0,-1],[1,0]]
    elif d==2:
        romal=[[-1,0],[0,-1]]
    elif d==3:
        romal=[[0, 1],[-1, 0]]
    for t in temp:
        nx=x+(romal[0][0]*t[0]+romal[0][1]*t[1])
        ny=y-(romal[1][0]*t[0]+romal[1][1]*t[1])
        if 0<=nx<=100 and 0<=ny<=100:
            grid[ny][nx]=1
    
ans=0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]:
            ans+=1

print(ans)