import sys
input = sys.stdin.readline

N,M,T=map(int, input().split())
circle=[list(map(int, input().split())) for _ in range(N)]

def rotate(x,d,k):
    if d==0: k=M-k
    for i in range(0,N+1,x):
        if i==0: continue
        circle[i-1]=circle[i-1][k:]+circle[i-1][:k]

def check():
    global circle
    flag=False
    temp=[c[:] for c in circle]
    for i in range(N):
        for j in range(M):
            if circle[i][j]==0: continue
            if i+1<N and circle[i+1][j]==circle[i][j]:
                temp[i][j],temp[i+1][j]=0,0
                flag=True
            if i-1>=0 and circle[i-1][j]==circle[i][j]:
                temp[i][j],temp[i-1][j]=0,0
                flag=True
            if j+1<=M and circle[i][(j+1)%M]==circle[i][j]:
                temp[i][j],temp[i][(j+1)%M]=0,0
                flag=True
            if j>=0 and circle[i][j-1]==circle[i][j]:
                temp[i][j],temp[i][j-1]=0,0
                flag=True
    circle=temp
    return flag

def adjust():
    num=sum(c.count(0) for c in circle)
    if num==N*M: return
    SUM=sum(map(sum, circle))
    avg=SUM/(M*N-num)
    for i in range(N):
        for j in range(M):
            if circle[i][j]>avg:
                circle[i][j]-=1
            elif 0<circle[i][j]<avg:
                circle[i][j]+=1

for _ in range(T):
    x,d,k=map(int, input().split())
    rotate(x,d,k)
    if not check(): adjust()
print(sum(map(sum, circle)))