import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans=N*M
cctv=[]
office=[]
for i in range(N):
    line = list(map(int, input().split()))
    office.append(line)
    for j in range(M):
        if line[j]!=0 and line[j]!=6: cctv.append([i,j]); ans-=1
        elif line[j]==6: ans-=1

def right(office, cctv):
    global ans
    x,y = cctv
    while True:
        if y+1>=M or office[x][y+1]==6: break
        elif office[x][y+1]==0: office[x][y+1]=-1; ans-=1
        y+=1

def left(office, cctv):
    global ans
    x,y = cctv
    while True:
        if y-1<0 or office[x][y-1]==6: break
        elif office[x][y-1]==0: office[x][y-1]=-1; ans-=1
        y-=1

def up(office, cctv):
    global ans
    x,y = cctv
    while True:
        if x+1>=N or office[x+1][y]==6: break
        elif office[x+1][y]==0: office[x+1][y]=-1; ans-=1
        x+=1

def down(office, cctv):
    global ans
    x,y = cctv
    while True:
        if x-1<0 or office[x-1][y]==6: break
        elif office[x-1][y]==0: office[x-1][y]=-1; ans-=1
        x-=1

def removeone(office, cctv, type):
    if type==1:
        right(office, cctv)
    if type==2:
        left(office, cctv)
    if type==3:
        up(office, cctv)
    if type==4:
        down(office, cctv)

def removetwo(office, cctv, type):
    if type==1:
        right(office, cctv)
        left(office, cctv)
    if type==2:
        up(office, cctv)
        down(office, cctv)

def removethree(office, cctv, type):
    if type==1:
        up(office, cctv)
        right(office, cctv)
    if type==2:
        down(office, cctv)
        right(office, cctv)
    if type==3:
        left(office, cctv)
        down(office, cctv)
    if type==4:
        left(office, cctv)
        up(office, cctv)

def removefour(office, cctv, type):
    if type==1:
        left(office, cctv)
        up(office, cctv)
        right(office, cctv)
    if type==2:
        up(office, cctv)
        down(office, cctv)
        right(office, cctv)
    if type==3:
        left(office, cctv)
        down(office, cctv)
        right(office, cctv)
    if type==4:
        down(office, cctv)
        left(office, cctv)
        up(office, cctv)

def removefive(office, cctv):
    right(office, cctv)
    up(office, cctv)
    down(office, cctv)
    left(office, cctv)

MIN=M*N
def dfs(office, depth):
    global ans
    global MIN
    if depth==len(cctv):
        MIN=min(MIN, ans)
        return
    x,y = cctv[depth]
    if office[x][y]==1:
        for type in range(4):
            temp=[o[:] for o in office]
            t=ans
            removeone(temp, [x,y], type+1)
            dfs(temp, depth+1)
            ans=t
    if office[x][y]==2:
        for type in range(2):
            temp=[o[:] for o in office]
            t=ans
            removetwo(temp, [x,y], type+1)
            dfs(temp, depth+1)
            ans=t
    if office[x][y]==3:
        for type in range(4):
            temp=[o[:] for o in office]
            t=ans
            removethree(temp, [x,y], type+1)
            dfs(temp, depth+1)
            ans=t
    if office[x][y]==4:
        for type in range(4):
            temp=[o[:] for o in office]
            t=ans
            removefour(temp, [x,y], type+1)
            dfs(temp, depth+1)
            ans=t
    if office[x][y]==5:
        temp=[o[:] for o in office]
        t=ans
        removefive(temp, [x,y])
        dfs(temp, depth+1)
        ans=t

dfs(office, 0)
print(MIN)