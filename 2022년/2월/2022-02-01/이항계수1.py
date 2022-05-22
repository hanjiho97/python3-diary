import sys
input = sys.stdin.readline

N, K =map(int, input().split())

if K==0 or K==N:
    print(1)
else:
    A=1
    B=1
    for i in range(K):
        A*=N-i
        B*=K-i
    print(A//B)