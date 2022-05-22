import sys

input = sys.stdin.readline

a=[[1,2,3,4],[1,2,3,4],[4,5,6,7]]
ans=0
for b in a:
    ans+=sum(b)
print(ans)