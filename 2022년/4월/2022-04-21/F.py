import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    W=list(map(int, input().split()))
    start,end=0,n-1
    Alice,Bob=W[0],W[n-1]
    total=2
    ans=[]
    while start<end:
        if Alice==Bob:
            ans.append(total)
            total+=1
            end-=1
            Bob+=W[end]
        elif Alice>Bob:
            total+=1
            end-=1
            Bob+=W[end]
        else:
            total+=1
            start+=1
            Alice+=W[start]
    if ans: print(ans[-1])
    else: print(0)
