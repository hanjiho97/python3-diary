import sys
input = sys.stdin.readline
N = int(input())
paper=[list(map(int, input().split())) for _ in range(N)]

blue=0
white=0

def cutting(paper, N):
    global blue
    global white
    if check(paper)==N*N:
        blue+=1
        return
    elif check(paper)==0:
        white+=1
        return
    one=[]
    two=[]
    three=[]
    four=[]
    for i in range(N//2):
        one.append(paper[i][:N//2])
        two.append(paper[i][N//2:])
        three.append(paper[N//2+i][:N//2])
        four.append(paper[N//2+i][N//2:])
    return cutting(one, N//2), cutting(two, N//2), cutting(three, N//2), cutting(four, N//2)


def check(paper):
    result=0
    for p in paper:
        result+=sum(p)
    return result

cutting(paper, N)

print(white)
print(blue)