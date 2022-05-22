import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
loc=list(map(int, input().split()))
num=deque([i+1 for i in range(N)])
count=0

for l in loc:
    if num.index(l)<=N-1-num.index(l):
        for _ in range(num.index(l)):
            num.append(num.popleft())
            count+=1
    else:
        for _ in range(N-num.index(l)):
            num.appendleft(num.pop())
            count+=1
    num.popleft()
    N-=1
print(count)