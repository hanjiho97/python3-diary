import sys
input = sys.stdin.readline
N, M = map(int, input().split())
l = sorted(map(int, input().split()))
used=[1]*N

ans=set([])
def generate(chosen, used):
    if len(chosen)==M:
        print(*chosen)
        return
    pre=-1
    for i in range(N):
        if used[i] and pre!=l[i]:
            pre=l[i]
            chosen.append(l[i])
            used[i]=0
            generate(chosen, used)
            used[i]=1
            chosen.pop()

generate([], used)