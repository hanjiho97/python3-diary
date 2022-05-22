import sys
import heapq as hq
input = sys.stdin.readline

heap=[]
for _ in range(int(input())):
    cmd=int(input())
    if not cmd:
        if heap:
            print(-hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, -cmd)