import sys
from collections import deque
input = sys.stdin.readline

card = deque([i+1 for i in range(int(input()))])

while len(card)!=1:
    card.popleft()
    card.append(card.popleft())

print(*card)