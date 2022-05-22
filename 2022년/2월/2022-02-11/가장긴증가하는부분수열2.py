import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def binsearch(target, start, end):
    while start<=end:
        mid=(start+end)//2
        if B[mid]>=target:
            end=mid-1
        else:
            start=mid+1
    return start

B=[A[0]]
for a in A:
    if B[-1]<a: B.append(a)
    else:
        B[binsearch(a, 0, len(B)-1)]=a
print(len(B))