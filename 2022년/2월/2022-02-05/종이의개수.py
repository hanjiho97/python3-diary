import sys
input = sys.stdin.readline

N = int(input())
paper=[list(map(int, input().split())) for _ in range(N)]

first=0
second=0
thrid=0
def cutting(paper, N):
    global first
    global second
    global thrid
    default=paper[0][0]
    flag=1
    for p in paper:
        for s in p:
            if default!=s:
                flag=0
                break
    if flag:
        if default==-1:
            first+=1
        elif default==0:
            second+=1
        elif default==1:
            thrid+=1
        return
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    i=[]
    for j in range(N//3):
        a.append(paper[j][:N//3])
        b.append(paper[j][N//3:2*N//3])
        c.append(paper[j][2*N//3:])
        d.append(paper[j+N//3][:N//3])
        e.append(paper[j+N//3][N//3:2*N//3])
        f.append(paper[j+N//3][2*N//3:])
        g.append(paper[j+2*N//3][:N//3])
        h.append(paper[j+2*N//3][N//3:2*N//3])
        i.append(paper[j+2*N//3][2*N//3:])
    return cutting(a, N//3), cutting(b, N//3), cutting(c, N//3), cutting(d, N//3), cutting(e, N//3), cutting(f, N//3), cutting(g, N//3), cutting(h, N//3), cutting(i, N//3)

cutting(paper, N)
print(first)
print(second)
print(thrid)