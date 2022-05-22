import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    priority=deque(list(map(int, input().split())))
    order=deque([i for i in range(N)])
    count=1
    for _ in range(N):
        if M==order[priority.index(max(priority))]:
            break
        for _ in range(priority.index(max(priority))):
            order.append(order.popleft())
            priority.append(priority.popleft())
        order.popleft()
        priority.popleft()
        count+=1
    print(count)