import sys
from collections import deque
input = sys.stdin.readline
data=deque()

for _ in range(int(input())):
    com = input().split()
    if com[0]=='push_back':
        data.append(int(com[1]))
    elif com[0]=='push_front':
        data.appendleft(int(com[1]))
    elif com[0]=='pop_front':
        if data:
            print(data.popleft())
        else:
            print(-1)
    elif com[0]=='pop_back':
        if data:
            print(data.pop())
        else:
            print(-1)
    elif com[0]=='size':
        print(len(data))
    elif com[0]=='empty':
        if data:
            print(0)
        else:
            print(1)
    elif com[0]=='front':
        if data:
            print(data[0])
        else:
            print(-1)
    elif com[0]=='back':
        if data:
            print(data[-1])
        else:
            print(-1)