import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
station = list(map(int, input().split()))

temp=distance[0]
cost=station[0]
total=0 
for i in range(N-2):
    if cost>station[i+1]:
        total+=cost*temp
        cost=station[i+1]
        temp=distance[i+1]
    else:
        temp+=distance[i+1]
total+=cost*temp
print(total)