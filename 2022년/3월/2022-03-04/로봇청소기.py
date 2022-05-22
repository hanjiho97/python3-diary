import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

maps=[]
for _ in range(N):
    maps.append(list(map(int, input().split())))

count=0
def cleaning(r, c, d, maps):
    global count
    if maps[r][c]==0:
        maps[r][c]=2
        count+=1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for _ in range(4):
        d=(d+3)%4
        x=r+dx[d]
        y=c+dy[d]
        if maps[x][y]==0:
            return cleaning(x, y, d, maps)
    x=r-dx[d]
    y=c-dy[d]
    if x<0 or x>=N or y<0 or y>=M: return
    elif maps[x][y]==1: return
    else: return cleaning(x, y, d, maps)

cleaning(r, c, d, maps)
print(count)