import sys
input=sys.stdin.readline

N,M=map(int,input().split())
num=list(map(int, input().split()))
sum,prefix=0,[0]
for n in num:
    sum+=n
    prefix.append(sum)
for _ in range(M):
    i,j=map(int,input().split())
    print(prefix[j]-prefix[i-1])