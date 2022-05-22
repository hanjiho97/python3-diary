import sys 
from collections import deque
input = sys.stdin.readline

def bfs(v):
    temp=deque([v])
    check[v]='B'
    turn=0
    while temp:
        l=len(temp)
        if turn%2:
            c='B'
        else:
            c='R'
        for _ in range(l):
            v=temp.popleft()
            for d in graph[v]:
                if check[d]=='0':
                    check[d]=c
                    temp.append(d)
                elif check[d]!=c:
                    return 1
        turn+=1
    return 0

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph=[[] for _ in range(V+1)]
    check=['0' for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    while True:
        try:
            if bfs(check.index('0', 1)):
                print('NO')
                break
            else:
                s='YES'
        except:
            print(s)
            break