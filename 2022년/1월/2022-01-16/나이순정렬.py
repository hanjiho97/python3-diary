import sys
input = sys.stdin.readline

data=[]
for _ in range(int(input())):
    data.append(input().split())
data.sort(key=lambda x: int(x[0]))
for d in data:
    print(' '.join(d))