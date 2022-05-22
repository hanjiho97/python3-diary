import sys
input = sys.stdin.readline

M, N = map(int, input().split())

pn = [False, False]+[True]*N

#소수표현
for i in range(2, int(N**0.5)+1):
    if pn[i]:
        for j in range(i*2, N+1, i):
            pn[j]=False

for i in range(M, N+1):
    if pn[i]:
        print(i)