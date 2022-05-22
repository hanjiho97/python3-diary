import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A=[list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j]%=1000

def involution(A, B):
    if B==1:
        return A
    m=involution(A, B//2)
    if B%2:
        return multiply(multiply(m, m), A)
    else:
        return multiply(m, m)

def multiply(A, B):
    global N
    result=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j]+=A[i][k]*B[k][j]
            result[i][j]%=1000
    return result

ans = involution(A, B)
for a in ans:
    print(*a)