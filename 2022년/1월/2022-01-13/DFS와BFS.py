import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

data=[[] for _ in range(N)]

#데이터 받기
for _ in range(M):
    x, y = map(int, input().split())
    data[x-1].append(y-1)
    data[y-1].append(x-1)

#데이터 정렬
for d in data:
    d.sort(reverse=True)

def dfs(v):
    seen=[0]*N
    stack=[v]
    while stack:
        v=stack.pop()
        if not seen[v]:
            seen[v]=1
            print(v+1, end=' ')
            stack+=data[v]

def bfs(v):
    seen=[0]*N
    temp=deque([v])
    seen[v]=1
    while temp:
        v = temp.popleft()
        print(v+1, end=' ')
        for d in reversed(data[v]):
            if not seen[d]:
                temp.append(d)
                seen[d]=1

dfs(V-1)
print()
bfs(V-1)