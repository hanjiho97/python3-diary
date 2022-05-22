import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    if n>=m:
        print('NO')
        continue
    if sum(a)+n+max(a)-min(a)<=m: print('YES')
    else: print('NO')