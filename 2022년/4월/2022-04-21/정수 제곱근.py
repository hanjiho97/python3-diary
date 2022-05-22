import sys
input=sys.stdin.readline
n=int(input())

def sqrt(n):
    start,end=0,n
    q=(start+end)//2
    while start<end:
        if q**2==n: break
        elif q**2>n: end=q
        else: start=q+1
        q=(start+end)//2
    return q
print(sqrt(n))