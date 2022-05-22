import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    if n==5: print(2,1,1,1); continue
    if n%4==0:
        print(n//4, n//4, n//4, n//4)
    elif n%4==1:
        print(2,n-5,2,1)
    elif n%4==2:
        print(1,n-3,1,1)    
    elif n%4==3:
        print(2,n-5,2,1)    