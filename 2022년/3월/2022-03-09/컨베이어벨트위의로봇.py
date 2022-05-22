import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False]*N)

def move(belt, robot):
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i]=False
            robot[i+1]=True
            belt[i+1]-=1
    robot[N-1]=False
    return

step=1
while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1]=False
    move(belt, robot)
    if belt[0]: robot[0]=True; belt[0]-=1
    if belt.count(0)>=K: break
    step+=1

print(step)