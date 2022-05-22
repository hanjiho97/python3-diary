import sys
from typing import Counter
input = sys.stdin.readline

graph=[]
N=int(input())
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

def dfs(x, y):
    global N
    global counter
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if graph[x][y]==1:
        counter+=1
        graph[x][y]=0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

ans=0
result=[]

for i in range(N):
    for j in range(N):
        counter=0
        if dfs(i,j)==True:
            result.append(counter)
            ans+=1

print(ans)
print('\n'.join(map(str, sorted(result))))
