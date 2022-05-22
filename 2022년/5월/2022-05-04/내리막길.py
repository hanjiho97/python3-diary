import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

M,N=map(int, input().split())
plan=[list(map(int, input().split())) for _ in range(M)]
route=[[-1]*N for _ in range(M)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(start):
    x,y=start
    if x==M-1 and y==N-1: return 1
    if route[x][y]!=-1: return route[x][y]
    route[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N: continue
        if plan[nx][ny]<plan[x][y]: 
            print()
            for r in route:
                print(*r)
            route[x][y]+=dfs([nx,ny])
    return route[x][y]
dfs([0,0])
for r in route:
    print(*r)
print(route[0][0])