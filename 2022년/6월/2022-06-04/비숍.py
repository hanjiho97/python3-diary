import sys
input = sys.stdin.readline

N=int(input())
board=[list(map(int, input().split())) for _ in range(N)]
visited=[0]*(2*N-1)
num,ans=0,0
total=0

def checking(n):
    if n>=2*N-1: return 0

    ans=-1
    if n<N: x=n; y=0
    else: x=N-1; y=n-(N-1)

    while x>=0 and y<N:
        if board[x][y] and not visited[y-x+N-1]:
            visited[y-x+N-1]=1
            num=checking(n+2)+1
            ans=max(ans,num)
            visited[y-x+N-1]=0
        x-=1
        y+=1
    if ans<0: ans=checking(n+2)
    return ans
print(checking(0)+checking(1))
        
