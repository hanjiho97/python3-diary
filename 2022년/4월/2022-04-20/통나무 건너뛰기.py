import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    L=list(map(int, input().split()))
    L.sort(reverse=True)
    ans=max(L[0]-L[2],L[N-2]-L[N-1])
    right,left=L[1],L[2]
    for i in range(3,len(L)):
        if i%2:
            ans=max(ans,right-L[i])
            right=L[i]
        else:
            ans=max(ans,left-L[i])
            left=L[i]
    print(ans)