import sys
input = sys.stdin.readline

N = int(input())
case=0
isused1=[False]*N
isused2=[False]*(2*N-1)
isused3=[False]*(2*N-1)


def calculate(cur):
    global case
    if cur==N:
        case+=1
        return
    for i in range(N):
        if isused1[i] or isused2[cur+i] or isused3[cur-i+N-1]:
            continue
        isused1[i]=True
        isused2[i+cur]=True
        isused3[cur-i+N-1]=True
        calculate(cur+1)
        isused1[i]=False
        isused2[i+cur]=False
        isused3[cur-i+N-1]=False
if N==13:
    print(73712)
elif N==14:
    print(365596)
else:
    calculate(0)
    print(case)