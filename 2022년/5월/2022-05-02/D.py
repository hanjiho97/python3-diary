import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=sorted(a)
    if n%2: 
        if a[0]!=b[0]: print('NO')
    elif a[0]!=b[0] and a[1]!=b[0]: print('NO')
    
