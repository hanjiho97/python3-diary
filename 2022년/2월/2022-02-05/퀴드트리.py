import sys
input = sys.stdin.readline

N = int(input())
video=[input().rstrip() for _ in range(N)]

def zipping(video, N):
    if check(video)==N*N:
        return '1'
    elif check(video)==0:
        return '0'
    leftup=[]
    rightup=[]
    leftbot=[]
    rightbot=[]
    for i in range(N//2):
        leftup.append(video[i][:N//2])
        rightup.append(video[i][N//2:])
        leftbot.append(video[i+N//2][:N//2])
        rightbot.append(video[i+N//2][N//2:])
    return '('+zipping(leftup, N//2)+zipping(rightup, N//2)+zipping(leftbot, N//2)+zipping(rightbot, N//2)+')'


def check(video):
    result=0
    for v in video:
        for s in v:
            result+=int(s)
    return result

print(zipping(video, N))