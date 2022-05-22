import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = sorted(map(int, input().split()))

def generate(chosen):
    if len(chosen)==M:
        print(*chosen)
        return
    for i in range(len(l)):
        if not chosen: chosen.append(l[i])
        elif chosen[-1]<=l[i]:
                chosen.append(l[i])
        else: continue
        generate(chosen)
        chosen.pop()

generate([])