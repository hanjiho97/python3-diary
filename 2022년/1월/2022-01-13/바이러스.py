import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

data=[[] for _ in range(V+1)]

#데이터 받기
for _ in range(E):
    v1, v2 = map(int, input().split())
    data[v1].append(v2)
    data[v2].append(v1)

def dfs(v):
    seen=[False]*(V+1)
    stack=[v]
    result=0
    while stack:
        v=stack.pop()
        if not seen[v]:
            seen[v]=True
            result+=1
            stack+=data[v]
    return result

print(dfs(1)-1)

