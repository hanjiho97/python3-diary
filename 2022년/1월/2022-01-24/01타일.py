import sys
from collections import deque
input = sys.stdin.readline

dp=deque()

#N이 1인경우 1밖에 못들어간다.
dp.append(1)
#N이 2인경우 11과 00이 가능하다.
dp.append(2)

#N이 3이상인 경우는 N-1에서 1이 더해진 경우와 
#N-2에서 11이나 00이 더해진 경우이다.
# 하지만 11이 더해진 경우는 N-1에서 1이 더해진 경우와 겹치기 때문에 제외한다.

N = int(input())

for i in range(2, N):
    dp.append((dp[0]+dp[1])%15746)
    dp.popleft()

if N==1:
    print(1)
else:
    print(dp[-1])