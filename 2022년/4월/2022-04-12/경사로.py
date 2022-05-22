import sys
input=sys.stdin.readline

N,L=map(int, input().split())
ground=[list(map(int, input().split())) for _ in range(N)]
road=0

def check(ground):
    global road
    for g in ground:
        Need=False
        Flag=True
        cnt=1
        for i in range(N-1):
            if abs(g[i]-g[i+1])>1: 
                Flag=False
                break
            elif g[i]-g[i+1]==0:
                cnt+=1
                if Need and cnt>=L:
                    Need=False
                    cnt=0
            elif g[i]-g[i+1]==-1:
                if Need or cnt<L: Flag=False; break
                cnt=1
            elif g[i]-g[i+1]==1:
                if Need: Flag=False; break
                if L>1: Need=True; cnt=1
                else: cnt=0
        if Flag and not Need: road+=1

check(ground)
ground=list(map(list, zip(*ground)))
check(ground)
print(road)