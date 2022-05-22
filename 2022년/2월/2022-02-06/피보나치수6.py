import sys
input = sys.stdin.readline

n = int(input())

def matmul(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j]+=A[i][k]*B[k][j]
            result[i][j]%=1000000007
    return result

def fibonacci(n):
    A=[[1,1],[1,0]]
    if n==1:
        return A
    m = fibonacci(n//2)
    if n%2:
        return matmul(matmul(m, m), A)
    else:
        return matmul(m, m)

print(fibonacci(n)[1][0])