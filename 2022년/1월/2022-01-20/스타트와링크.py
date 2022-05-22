import sys
input = sys.stdin.readline

N = int(input())
graph=[list(map(int, input().split())) for _ in range(N)]

team = [i for i in range(N)]
min=1000

def divide(chosen):
    global min
    if len(chosen)==N//2:
        #그룹나누기
        start = chosen
        link = list(set(team) - set(chosen))
        #각 능력치 계산
        ss=0
        sl=0
        for i in start:
            for j in start:
                ss+=graph[i][j]
        for i in link:
            for j in link:
                sl+=graph[i][j]
        #최소값인지 확인
        if abs(ss-sl)<min:
            min=abs(ss-sl)
        return
    first = team.index(chosen[-1])+1 if chosen else 0
    for i in range(first, len(team)):
        chosen.append(team[i])
        divide(chosen)
        chosen.pop()

divide([])
print(min)