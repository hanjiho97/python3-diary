from math import sqrt
N,W,H = map(int, input().split())
D=int(sqrt(W**2+H**2))
for _ in range(N):
    d=int(input())
    if d<=D: print('DA')
    else: print('NE')