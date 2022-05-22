import sys
input = sys.stdin.readline

wheel=[]
for _ in range(4):
    wheel.append(input().rstrip())

def rotate(n, dir):
    if dir==1:
        wheel[n-1]=wheel[n-1][-1]+wheel[n-1][:7]
    elif dir==-1:
        wheel[n-1]=wheel[n-1][1:]+wheel[n-1][0]

def check(n):
    connection=[0,0,0]
    for i in range(3):
        if wheel[i][2]!=wheel[i+1][6]:
            connection[i]=1
    temp=set()
    for i in range(3):
        if connection[i]: temp.add(i+1); temp.add(i+2)
        else:
            if n in temp: return temp
            else: temp=set()
    if n in temp: return temp
    else: return False

for _ in range(int(input())):
    n, dir = map(int, input().split())
    todo=check(n)
    if not todo: rotate(n, dir)
    else:
        for t in todo:
            if abs(t-n)%2: rotate(t, -dir)
            else: rotate(t, dir)

print(int(wheel[0][0])+int(wheel[1][0])*2+int(wheel[2][0])*4+int(wheel[3][0])*8)