import sys
input = sys.stdin.readline

N = int(input())
pos=[[0]*N for _ in range(N)]

def check(x, y , stud):
    count1=0
    count2=0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N: continue
        if pos[nx][ny] in stud: count1+=1
        if pos[nx][ny]==0: count2+=1
    return count1, count2

student=[]
for _ in range(N**2):
    student.append(list(map(int, input().split())))

order=[]
for k in range(N**2):
    temp=[]
    curmax1=0
    curmax2=0
    for i in range(N):
        for j in range(N):
            if not pos[i][j]:
                c1, c2 = check(i, j, student[k][1:])
                if c1>curmax1:
                    temp=[[i, j]]
                    curmax1=c1
                    curmax2=c2
                elif c1==curmax1:
                    if c2>curmax2:
                        temp=[[i, j]]
                        curmax1=c1
                        curmax2=c2
                    elif c2==curmax2:
                        temp.append([i,j])
    temp.sort()
    order.append([temp[0][0], temp[0][1]])
    pos[temp[0][0]][temp[0][1]]=student[k][0]

ans=0
for i in range(N**2):
    c1, c2 = check(order[i][0], order[i][1], student[i][1:])
    if c1==0: continue
    elif c1==1: ans+=1
    elif c1==2: ans+=10
    elif c1==3: ans+=100
    elif c1==4: ans+=1000      

print(ans) 