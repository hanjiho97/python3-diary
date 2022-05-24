import sys
from collections import deque
input = sys.stdin.readline

N,M,R=map(int, input().split())
visited=[0]*(N+1)
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort(reverse=True)

def bfs(v):
    temp=deque([v])
    cnt=1
    visited[v]=cnt
    while temp:
        s=temp.popleft()
        for g in graph[s]:
            if not visited[g]:
                cnt+=1
                visited[g]=cnt
                temp.append(g)
bfs(R)
print('\n'.join(map(str, visited[1:])))