import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l=[i+1 for i in range(N)]

def generate(chosen):
    global start
    if len(chosen)==M:
        print(*chosen)
        return
    start=l.index(chosen[-1]) if chosen else 0
    for i in range(start, N):
        chosen.append(l[i])
        generate(chosen)
        chosen.pop()
        
generate([])