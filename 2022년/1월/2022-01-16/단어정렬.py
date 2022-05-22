import sys
input = sys.stdin.readline

data=set()
for _ in range(int(input())):
    data.add(input())
data=list(data)
data.sort()
data.sort(key=lambda x: len(x))
print(''.join(data))