import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix1=[list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
matrix2=[list(map(int, input().split())) for _ in range(M)]

result=[[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j]+=(matrix1[i][k]*matrix2[k][j])
for r in result:
    print(*r)