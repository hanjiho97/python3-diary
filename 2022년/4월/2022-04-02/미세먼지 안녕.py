import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A=[list(map(int, input().split())) for _ in range(R)]
pos=[]
for i in range(R):
    if A[i][0]==-1:
        pos.append(i)

def spread(A):
    temp=[[0]*C for _ in range(R)]
    temp[pos[0]][0],temp[pos[1]][0] = -1,-1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(R):
        for j in range(C):
            if not A[i][j] or A[i][j]==-1: continue
            dust=A[i][j]//5
            count=0
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if nx<0 or nx>=R or ny<0 or ny>=C or A[nx][ny]==-1: continue
                temp[nx][ny]+=dust
                count+=1
            temp[i][j]+=A[i][j]-dust*count
    return temp

def circulation(A):
    #윗바람
    LU,RD = A[0][0], A[pos[0]][C-1]
    A[pos[0]]=[-1,0]+A[pos[0]][1:C-1]
    A[0]=A[0][1:]+[0]
    for i in range(0, pos[0]-1):
        A[i][C-1]=A[i+1][C-1]
        A[pos[0]-1-i][0]=A[pos[0]-2-i][0]
    A[1][0],A[pos[0]-1][C-1] = LU,RD 
    #아랫바람
    RU,LD = A[pos[1]][C-1],A[R-1][0]
    A[pos[1]]=[-1,0]+A[pos[1]][1:C-1]
    A[R-1]=A[R-1][1:]+[0]
    for i in range(R-1, pos[1]+1, -1):
        A[i][C-1]=A[i-1][C-1]
        A[pos[1]+1+(R-1-i)][0]=A[pos[1]+1+(R-i)][0]
    A[R-2][0],A[pos[1]+1][C-1] = LD,RU
    return

for _ in range(T):
    A=spread(A)
    circulation(A)

ans=2
for a in A:
    ans+=sum(a)
print(ans)