import sys
input = sys.stdin.readline

data=[]
for _ in range(int(input())):
    command = input().split()
    if command[0]=='push':
        data.append(command[1])
    if command[0]=='pop':
        if data:
            print(data.pop())
        else:
            print(-1)
    if command[0]=='size':
        print(len(data))
    if command[0]=='empty':
        if data:
            print(0)
        else:
            print(1)
    if command[0]=='top':
        if data:
            print(data[-1])
        else:
            print(-1)