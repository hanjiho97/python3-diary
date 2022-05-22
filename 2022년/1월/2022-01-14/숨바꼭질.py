import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

def bfs(n, m):
    temp=deque([n])
    while temp:
        v=temp.popleft()
        if(v==m):
            print(time[v])
            return
        for nv in (v-1, v+1, v*2):
            if 0<=nv<100001 and not time[nv]:
                time[nv]=time[v]+1
                temp.append(nv)

time=[0]*100001
bfs(N, M)