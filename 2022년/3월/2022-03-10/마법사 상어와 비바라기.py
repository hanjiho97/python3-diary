import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

def watercopy(A, cloud):
    for x, y in cloud:
        count=0
        for i in range(4):
            nx=x+dx[1+i*2]
            ny=y+dy[1+i*2]
            if 0<=nx<N and 0<=ny<N and A[nx][ny]: count+=1
        A[x][y]+=count
    return

for _ in range(M):
    d, s = map(int, input().split())
    visited=[[False]*N for _ in range(N)]
    for i in range(len(cloud)):
        cloud[i][0]=(cloud[i][0]+dx[d-1]*s)%N
        cloud[i][1]=(cloud[i][1]+dy[d-1]*s)%N
        A[cloud[i][0]][cloud[i][1]]+=1
        visited[cloud[i][0]][cloud[i][1]]=True
    watercopy(A, cloud)
    cloud=[]
    for i in range(N):
        for j in range(N):
            if A[i][j]>=2 and not visited[i][j]:
                cloud.append([i,j])
                A[i][j]-=2

print(sum(sum(a) for a in A))