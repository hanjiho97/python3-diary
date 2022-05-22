import sys
input=sys.stdin.readline

n,k=map(int, input().split())
case=[1]+[0]*k
for _ in range(n):
    c=int(input())
    for i in range(k+1):
        if case[i] and i+c<=k:
            case[i+c]+=case[i]
print(case[k])