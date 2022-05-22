import sys
import heapq as hq
input = sys.stdin.readline

heap=[]
for _ in range(int(input())):
    cmd = int(input())
    if cmd>0: hq.heappush(heap, [cmd, 1])
    elif cmd<0: hq.heappush(heap, [-cmd, -1])
    else: 
        if heap:
            a=hq.heappop(heap)
            print(a[0]*a[1])
        else: print(0)