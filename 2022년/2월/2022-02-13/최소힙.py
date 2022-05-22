import sys
import heapq as hq
input = sys.stdin.readline

heap=[]
for _ in range(int(input())):
    cmd=int(input())
    if cmd: hq.heappush(heap, cmd)
    else:
        if heap: print(hq.heappop(heap))
        else: print(0)