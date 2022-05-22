import sys
import heapq as hq
input = sys.stdin.readline
heap1, heap2 = [], []
for i in range(int(input())):
    a=int(input())
    if not heap2 or a>=heap2[0]: hq.heappush(heap2, a)
    else: hq.heappush(heap1, -a)
    if len(heap2)-2>len(heap1): hq.heappush(heap1, -hq.heappop(heap2))
    elif len(heap2)-1<len(heap1): hq.heappush(heap2, -hq.heappop(heap1))
    print(heap2[0])