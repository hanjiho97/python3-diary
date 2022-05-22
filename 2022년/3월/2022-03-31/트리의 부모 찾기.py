import sys
input = sys.stdin.readline

N=int(input())
data=[[] for _ in range(N)]
parent=[0]*N

for _ in range(N-1):
    a,b=map(int, input().split())
    data[a-1].append(b-1)
    data[b-1].append(a-1)

def dfs(v):
    seen=[0]*N
    stack=[v]
    while stack:
        v=stack.pop()
        for d in data[v]:
            if not seen[d]:
                seen[d]=1
                parent[d]=v+1
                stack.append(d)

dfs(0)

print('\n'.join(map(str, parent[1:])))