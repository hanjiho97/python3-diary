import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
num = deque([i+1 for i in range(N)])

print("<", end='')
for i in range(N-1):
    for _ in range(K-1):
        num.append(num.popleft())
    print(num.popleft(), end=', ')
print(num[0], end='>\n')