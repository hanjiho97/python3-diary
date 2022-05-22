import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    counter=[0]*(n+1)
    A=list(map(int, input().split()))
    flag=True
    for a in A:
        counter[a]+=1
        if counter[a]>=3:
            print(a)
            flag=False
            break
    if flag: print(-1)