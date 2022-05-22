import sys
input = sys.stdin.readline

N = int(input())

def d(n):
    L = str(n)
    sum = 0
    for l in L:
        sum+=int(l)
    sum+=n
    return sum

M=N-(len(str(N)))*9

for i in range(max(0,M), N+1):
    if(d(i)==N):
        print(i)
        break
    else:
        if(i==N):
            print(0)