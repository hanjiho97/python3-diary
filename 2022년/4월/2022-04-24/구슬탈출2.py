import sys
input = sys.stdin.readline

N,M=map(int,input().split())
board=[]
for i in range(N):
    board.append(list(input().rstrip()))
    for j in range(M):
        if board[i][j]=='R': red=[i,j]; board[i][j]='.'
        elif board[i][j]=='B': blue=[i,j]; board[i][j]='.'
        elif board[i][j]=='O': goal=[i,j]
ans=11

def left(red,blue):
    first,second=red,blue
    if red[0]==blue[0] and red[1]>blue[1]:
        first,second=blue,red
    x,y=first
    while first!=goal:
        y-=1
        if y<0 or board[x][y]=='#': 
            board[x][y+1]='#'
            break
        first[0],first[1]=x,y
    x,y=second
    while second!=goal:
        y-=1
        if y<0 or board[x][y]=='#': break
        second[0],second[1]=x,y
    board[first[0]][first[1]]='.'
    return red,blue

def right(red,blue):
    first,second=red,blue
    if red[0]==blue[0] and red[1]<blue[1]:
        first,second=blue,red
    x,y=first
    while first!=goal:
        y+=1
        if y>=M or board[x][y]=='#': 
            board[x][y-1]='#'
            break
        first[0],first[1]=x,y
    x,y=second
    while second!=goal:
        y+=1
        if y>=M or board[x][y]=='#': break
        second[0],second[1]=x,y
    board[first[0]][first[1]]='.'
    return red,blue


def up(red,blue):
    first,second=red,blue
    if red[1]==blue[1] and red[0]>blue[0]:
        first,second=blue,red
    x,y=first
    while first!=goal:
        x-=1
        if x<0 or board[x][y]=='#': 
            board[x+1][y]='#'
            break
        first[0],first[1]=x,y
    x,y=second
    while second!=goal:
        x-=1
        if x<0 or board[x][y]=='#': break
        second[0],second[1]=x,y
    board[first[0]][first[1]]='.'
    return red,blue

def down(red,blue):
    first,second=red,blue
    if red[1]==blue[1] and red[0]<blue[0]:
        first,second=blue,red
    x,y=first
    while first!=goal:
        x+=1
        if x>=M or board[x][y]=='#': 
            board[x-1][y]='#'
            break
        first[0],first[1]=x,y
    x,y=second
    while second!=goal:
        x+=1
        if x>=M or board[x][y]=='#': break
        second[0],second[1]=x,y
    board[first[0]][first[1]]='.'
    return red,blue

def solve(red,blue,count):
    global ans
    if count>10 or blue==goal: return
    if red==goal:
        ans=min(ans, count)
        return
    temp1,temp2=red[:],blue[:]
    temp1,temp2=left(temp1,temp2)
    solve(temp1,temp2,count+1)
    temp1,temp2=red[:],blue[:]
    temp1,temp2=right(temp1,temp2)
    solve(temp1,temp2,count+1)
    temp1,temp2=red[:],blue[:]
    temp1,temp2=up(temp1,temp2)
    solve(temp1,temp2,count+1)
    temp1,temp2=red[:],blue[:]
    temp1,temp2=down(temp1,temp2)
    solve(temp1,temp2,count+1)

solve(red,blue,0)
if ans==11: print(-1)
else: print(ans)