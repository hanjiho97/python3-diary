import sys
input = sys.stdin.readline
N, M = map(int, input().split())
l = sorted(map(int, input().split()))
def generate(chosen, start):
    if len(chosen)==M:
        print(*chosen)
        return
    pre=-1
    for i in range(start, N):
        if pre!=l[i]:
            pre=l[i]
            chosen.append(l[i])
            generate(chosen, i)
            chosen.pop()
generate([], 0)