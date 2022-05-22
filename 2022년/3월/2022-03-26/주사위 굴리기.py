import sys
from collections import deque
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
diceUD=deque([0,0,0,MAP[x][y]])
diceLR=deque([0,0,0,MAP[x][y]])
dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]
for cmd in map(int, input().split()):
    if x+dx[cmd]<0 or y+dy[cmd]<0 or x+dx[cmd]>=N or y+dy[cmd]>=M: continue
    x+=dx[cmd]
    y+=dy[cmd]
    if cmd==1:
        diceLR.rotate(1)
        diceUD[1], diceUD[-1]=diceLR[1], diceLR[-1]
    elif cmd==2:
        diceLR.rotate(-1)
        diceUD[1], diceUD[-1]=diceLR[1], diceLR[-1]
    elif cmd==3:
        diceUD.rotate(-1)
        diceLR[1], diceLR[-1]=diceUD[1], diceUD[-1]
    elif cmd==4:
        diceUD.rotate(1)
        diceLR[1], diceLR[-1]=diceUD[1], diceUD[-1]
    if MAP[x][y]:
        diceUD[-1], diceLR[-1]=MAP[x][y], MAP[x][y]
        MAP[x][y]=0
    else: MAP[x][y]=diceUD[-1]
    print(diceUD[1])