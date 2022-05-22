import sys
input=sys.stdin.readline
N,M=map(int, input().split())
pocket=dict()
rpocket=dict()
for i in range(1, N+1):
    name=input().rstrip()
    pocket[name]=i
    rpocket[i]=name
for _ in range(M):
    target=input().rstrip()
    if target.isdigit(): print(rpocket[int(target)])
    else: print(pocket[target])