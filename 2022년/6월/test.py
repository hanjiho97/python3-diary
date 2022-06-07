import sys
input = sys.stdin.readline

N=int(input())
board=[list(map(int, input().split())) for _ in range(N)]
visited1=[0]*(2*N-1)
visited2=[0]*(2*N-1)

def checking(n):
    global num, ans
    ans=max(ans,num)
    for i in range(start,2*N-1,2):
        if visited1[i]: continue
        if i<N:
            for j in range(i+1):
                if visited2[2*j-i+N-1] or not board[i-j][j]: continue
                visited1[i],visited2[2*j-i+N-1]=1,1
                board[i-j][j]=0
                num+=1
                checking(start,board)
                visited1[i],visited2[2*j-i+N-1]=0,0
                board[i-j][j]=1
                num-=1
        else:
            i-=N-1
            for j in range(i, N):
                if visited2[2*j-i] or not board[N-1+i-j][j]: continue
                visited1[N-1+i],visited2[2*j-i]=1,1
                board[N-1+i-j][j]=0
                num+=1
                checking(start,board)
                visited1[N-1+i],visited2[2*j-i]=0,0
                board[N-1+i-j][j]=1
                num-=1

checking(0,board)
total+=ans
num,ans=0,0
checking(1,board)
total+=ans
print(total)