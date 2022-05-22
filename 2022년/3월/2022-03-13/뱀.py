import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board=[[0]*(N+1) for _ in range(N+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x][y]=2

def move(snake, board, dir):
    dx=[0,-1,0,1]
    dy=[1,0,-1,0]
    x, y = snake[0][0], snake[0][1]
    nx = x+dx[dir]
    ny = y+dy[dir]
    if nx<1 or nx>N or ny<1 or ny>N or board[nx][ny]==1: 
        return False
    snake.appendleft([nx, ny])
    if board[nx][ny]==0:
        x, y = snake.pop()
        board[x][y]=0
    board[nx][ny]=1
    return True

board[1][1]=1
snake=deque([[1,1]])
dir=0
time=0
for _ in range(int(input())):
    s, d = input().split()
    for _ in range(int(s)-time):
        if not move(snake, board, dir):
            print(time+1)
            exit()
        time+=1
    if d=='L': dir=(dir+1)%4
    else: dir=(dir+3)%4

while move(snake, board, dir):
    time+=1
print(time+1)