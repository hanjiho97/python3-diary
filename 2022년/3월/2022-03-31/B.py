import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    candies = sorted(map(int, input().split()), reverse=True)
    if n==1:
        if candies[0]==1: print('YES'); continue
        else: print('NO'); continue
    if candies[0]-candies[1]>1: print('NO')
    else: print('YES')