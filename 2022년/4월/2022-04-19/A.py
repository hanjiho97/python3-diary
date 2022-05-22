import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=0
    if (n==1 or m==1) and abs(m-n)>1: 
        print(-1)
        continue
    if n==m: ans+=(n-1)*2
    elif n>m: ans+=(m-1)*2+((n-m)//2)*4+(n-m)%2
    else: ans+=(n-1)*2+((m-n)//2)*4+(m-n)%2
    print(ans)