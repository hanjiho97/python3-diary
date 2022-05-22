import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = [i+1 for i in range(N)]
used = [0]*N

def generate(chosen, used):
    if len(chosen)==M:
        print(*chosen)
        return
    for i in range(len(l)):
        if not used[i]:
            chosen.append(l[i])
            used[i]=1
            generate(chosen, used)
            used[i]=0
            chosen.pop()

generate([], used)