import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house=[]
chicken=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1: house.append([i,j])
        elif city[i][j]==2: chicken.append([i,j])

chick_dist=[]
for i in range(len(house)):
    chick_dist.append([])
    for j in range(len(chicken)):
        chick_dist[i].append([(abs(house[i][0]-chicken[j][0])+abs(house[i][1]-chicken[j][1])), j])
    chick_dist[i].sort(key = lambda x: x[0])


ans=10000000
for chosen in combinations([i for i in range(len(chicken))], M):
    temp=0
    for cd in chick_dist:
        for c in cd:
            if c[1] in chosen:
                temp+=c[0]
                break
    ans = min(ans, temp)
print(ans)