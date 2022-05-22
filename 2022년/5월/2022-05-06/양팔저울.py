import sys
input=sys.stdin.readline

N=int(input())
W=list(map(int, input().split()))
M=int(input())
target=list(map(int, input().split()))

dp=set([0])
for i in range(N):
    temp=[]
    for d in dp:
        temp.append(d-W[i])
        temp.append(d+W[i])
    dp.update(temp)

for t in target:
    if t in dp: print('Y', end=' ')
    else: print('N', end=' ')