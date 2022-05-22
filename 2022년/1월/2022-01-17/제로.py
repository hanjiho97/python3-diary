import sys
input = sys.stdin.readline

data=[]
for _ in range(int(input())):
    N = int(input())
    if N: data.append(N)
    else: data.pop()

print(sum(data))