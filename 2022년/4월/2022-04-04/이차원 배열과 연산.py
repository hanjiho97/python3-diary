import sys
from collections import Counter
input = sys.stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
R, C = 3, 3

def Rcal(A):
    C=0
    for i in range(len(A)):
        count=dict(Counter(A[i]))
        if 0 in count: count.pop(0)
        count=sum(sorted(map(list,count.items()), key=lambda x: (x[1], x[0])), [])
        C=max(C, len(count))
        A[i]=count
    for i in range(len(A)):
        A[i]+=[0]*(C-len(A[i]))                
    return C

for sec in range(101):
    if r<=R and c<=C and A[r-1][c-1]==k: print(sec); exit()
    if R>=C: C=Rcal(A)
    else:
        A=list(map(list, zip(*A)))
        R=Rcal(A)
        A=list(map(list, zip(*A)))
print(-1)