import sys
input=sys.stdin.readline
N,M=map(int, input().split())
num=list(map(int, input().split()))

counter=[0]*M
counter[0]=1
s=0
for i in range(len(num)):
    s=(s+num[i])%M
    counter[s]+=1

cnt=0
for c in counter:
    if c>1: cnt+=((c)*(c-1)//2)
print(cnt)