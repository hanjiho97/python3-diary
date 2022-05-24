import sys
input = sys.stdin.readline
N,M=map(int, input().split())
board=[0]*101
counter=[100]*101
for _ in range(N+M):
    a,b=map(int, input().split())
    board[a]=b

def dfs(start, count):
    if start==100: return
    for i in range(1, 7):
        new=start+i
        if new>100 or count>=counter[new]: continue
        counter[new]=count
        if board[new]: new=board[new]
        dfs(new, count+1)

dfs(1, 1)
print(counter[100])