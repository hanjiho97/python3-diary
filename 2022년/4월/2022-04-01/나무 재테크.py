import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ground=[[5]*N for _ in range(N)]
tree=[[{} for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1][z]=1

def grow(ground, A, tree):
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    temp=[[{} for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                ground[i][j]+=A[i][j]
                continue
            bread=0
            death=0
            for age, count in sorted(tree[i][j].items()):
                num=ground[i][j]//age
                if num>=count: 
                    ground[i][j]-=age*count
                    temp[i][j][age+1]=count
                    if not (age+1)%5: bread+=count
                elif 0<num: 
                    ground[i][j]-=age*num
                    temp[i][j][age+1]=num
                    if not (age+1)%5: bread+=num
                    death+=(age//2)*(count-num)
                else:
                    death+=(age//2)*count
            if bread:
                for k in range(8):
                    nx,ny = i+dx[k],j+dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=N: continue
                    if 1 not in temp[nx][ny]:
                        temp[nx][ny][1]=0
                    temp[nx][ny][1]+=bread
            ground[i][j]+=(death+A[i][j])
    return temp

for _ in range(K):
    tree=grow(ground, A, tree)

ans=0
for i in range(N):
    for j in range(N):
        ans+=sum(tree[i][j].values())
print(ans)