import sys
input = sys.stdin.readline
M=int(input())
N=int(input())

if(M==1):
    pn=[False]+[True]*(N-M)
    sum=int(N*(N+1)/2-(M-1)*M/2)-1
else:
    pn=[True]*(N-M+1)
    sum=int(N*(N+1)/2-(M-1)*M/2)


for i in range(2, int((N**0.5)+1)):
    for j in range(M, N+1):
        if pn[j-M]:
            if(j%i==0):
                if(i!=j):
                    pn[j-M]= False
                    sum-=j

if sum==0:
    print(-1)
else:
    print(sum)
    print(pn.index(True)+M)