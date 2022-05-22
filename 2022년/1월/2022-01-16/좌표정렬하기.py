import sys
input = sys.stdin.readline

data=[]
for _ in range(int(input())):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1])
for d in data:
    print(' '.join(map(str, d)))