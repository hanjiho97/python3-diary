import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    ans=0
    cnt=2
    for c in s:
        if c=='1': cnt+=1
        else: ans+=max(2-cnt, 0); cnt=0
    print(ans)