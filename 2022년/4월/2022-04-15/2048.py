import sys
input = sys.stdin.readline

N=int(input())
board=[list(map(int, input().split())) for _ in range(N)]
ans=0

def right(board):
    for i in range(N):
        count,temp=0,[]
        for j in range(N-1,-1,-1):
            if board[i][j]==0: count+=1
            else: temp.append(board[i][j])
        temp+=[0]
        board[i],idx=[],0
        while idx<len(temp)-1:
            if temp[idx]==temp[idx+1]:
                board[i].append(temp[idx]*2)
                count+=1
                idx+=2
            else:
                board[i].append(temp[idx])
                idx+=1
        board[i].reverse()
        board[i]=[0]*count+board[i]
    return board

def left(board):
    for i in range(N):
        count,temp=0,[]
        for j in range(N):
            if board[i][j]==0: count+=1
            else: temp.append(board[i][j])
        temp+=[0]
        board[i],idx=[],0
        while idx<len(temp)-1:
            if temp[idx]==temp[idx+1]:
                board[i].append(temp[idx]*2)
                count+=1
                idx+=2
            else:
                board[i].append(temp[idx])
                idx+=1
        board[i]+=[0]*count
    return board

def up(board):
    temp=list(map(list, zip(*board)))
    temp=left(temp)
    temp=list(map(list, zip(*temp)))
    return temp

def down(board):
    temp=list(map(list, zip(*board)))
    temp=right(temp)
    temp=list(map(list, zip(*temp)))
    return temp

def solve(board, depth):
    global ans
    if depth==5:
        ans=max(ans, max(map(max, board)))
        return
    temp=[b[:] for b in board]
    temp=up(temp)
    solve(temp, depth+1)
    temp=[b[:] for b in board]
    temp=down(temp)
    solve(temp, depth+1)
    temp=[b[:] for b in board]
    temp=left(temp)
    solve(temp, depth+1)
    temp=[b[:] for b in board]
    temp=right(temp)
    solve(temp, depth+1)

solve(board, 0)
print(ans)