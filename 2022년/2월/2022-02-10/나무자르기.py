import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
tree = Counter(map(int, input().split()))

start = 0
end = max(tree)

while start<=end:
    mid=(start+end)//2
    total=0
    for t, n in tree.items():
        if t>mid:
            total+=(t-mid)*n
    if total<M:
        end=mid-1
    else:
        start=mid+1
print(start-1)