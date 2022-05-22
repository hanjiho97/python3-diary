import sys
input = sys.stdin.readline

N = int(input())
ring = list(map(int,input().split()))

def GCD(a, b):
    if a%b:
        return GCD(b, a%b)
    else:
        return b

ref=ring[0]
for i in range(1, N):
    A=GCD(max(ref, ring[i]), min(ref, ring[i]))
    print("%d/%d"%(ref//A, ring[i]//A))