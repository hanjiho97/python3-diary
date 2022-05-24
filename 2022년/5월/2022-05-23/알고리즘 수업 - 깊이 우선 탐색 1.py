import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,R=map(int, input().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count=1
def dfs(v):
    global count
    visited[v]=count
    for g in sorted(graph[v], reverse=True):
        if not visited[g]:
            count+=1
            dfs(g)
dfs(R)

print('\n'.join(map(str, visited[1:])))