import sys
input=sys.stdin.readline

V=int(input())
graph=[[] for _ in range(V+1)]
for _ in range(V):
    temp=list(map(int, input().split()[:-1]))
    graph[temp[0]]=temp[1:]


ans=0
node,distance=0,0
visited=[False]*(V+1)
def dfs(num):
    global ans,node,distance
    visited[num]=True
    for i in range(0,len(graph[num]),2):
        v,d=graph[num][i],graph[num][i+1]
        if visited[v]: continue
        distance+=d
        if ans<distance: ans,node=distance,v
        dfs(v)
        distance-=d
    visited[num]=False
    return 

dfs(1)
dfs(node)
print(ans)