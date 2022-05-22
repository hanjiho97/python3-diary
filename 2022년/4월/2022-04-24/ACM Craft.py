import sys
from collections import deque
input = sys.stdin.readline

def winningtime(W):
    cal=[0]*(N+1)
    q=deque()
    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            cal[i]=max(cal[i],time[now])
            if indegree[i]==0:
                time[i]+=cal[i]
                q.append(i)
                if i==W: return time[W]
    return time[W]

for _ in range(int(input())):
    N,K=map(int, input().split())
    time=[0]+list(map(int, input().split()))
    graph=[[] for _ in range(N+1)]
    indegree=[0]*(N+1)
    for _ in range(K):
        X,Y=map(int, input().split())
        graph[X].append(Y)
        indegree[Y]+=1
    W=int(input())
    print(winningtime(W))
