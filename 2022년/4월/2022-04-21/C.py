import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    check=[0]*4
    for i in range(n):
        if i%2:
            if a[i]%2: check[0]+=1
            else: check[1]+=1
        else:
            if a[i]%2: check[2]+=1
            else: check[3]+=1
    if (check[0]==0 or check[1]==0) and (check[2]==0 or check[3]==0):
        print('Yes')
    else: print('No')