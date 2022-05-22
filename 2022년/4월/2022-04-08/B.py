import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    cnt=dict(Counter(a))
    cnt=sorted(map(list,cnt.items()), key=lambda x: x[1], reverse=True)
    ans=0
    count=cnt[0][1]
    if count==n:
        print(ans); continue
    elif count%2==0:
        while True:
            ans+=1
            if count*2>=n:
                ans+=count//2
                break
            count*=2
    print(ans)