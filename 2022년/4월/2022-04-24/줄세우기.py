import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int, input().split())
graph=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
result=[]

def tosort():
    q=deque()
    for i in range(1,N+1):
        if indegree[i]==0: q.append(i)
    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0: q.append(i)

for _ in range(M):
    A,B=map(int, input().split())
    graph[B].append(A)
    indegree[A]+=1
tosort()
result.reverse()
print(*result)